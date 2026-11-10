"""Post-freeze paired analysis; no inference or dataset selection."""

import csv
import json
import sys
from collections import Counter
from pathlib import Path

RUN = Path("$ZEROSHOT_ARTIFACT_ROOT/revalue_generic_highlight_tvsum_val10_v1_2026-11-10")


def distribution(values):
    if not values:
        return None
    return dict(
        count=len(values),
        minimum=min(values),
        maximum=max(values),
        mean=sum(values) / len(values),
        unique=len(set(values)),
        le_005=sum(v <= 0.05 for v in values),
        ge_095=sum(v >= 0.95 for v in values),
        ge_050=sum(v >= 0.5 for v in values),
    )


def main():
    sys.path.insert(0, str(RUN / "source_snapshot"))
    import metrics
    from core import load_preparation, read_json, sha256, write_new
    from vendor.reze_core import extract_pyes, segments_to_curve

    manifest, rows = load_preparation(RUN)
    freeze = read_json(RUN / "prediction_freeze.json")
    if sha256(RUN / "predictions.json") != freeze["predictions_sha256"] or freeze["labels_read"] is not False:
        raise ValueError("New predictions must be frozen before comparison")
    if freeze["manifest_sha256"] != sha256(RUN / "manifest.json"):
        raise ValueError("Input binding changed")
    predictions = read_json(RUN / "predictions.json")
    binding = read_json(RUN / "comparison_binding.json")
    ids = read_json(RUN / "token_ids.json")
    baselines, old_values, old_modes, old_tokens, parity = {}, {}, Counter(), 0, []
    for row in rows:
        vid = row["vid"]
        reference = binding["baseline"][vid]
        path = Path(reference["path"])
        if sha256(path) != reference["sha256"]:
            raise ValueError("Historical baseline changed")
        baseline = read_json(path)
        shard = path.parent.parent
        media = read_json(shard / "media" / f"{vid}.json")
        chunks = sorted((shard / "chunks" / vid).glob("*.json"))
        values, checked = [], 0
        for chunk_path in chunks:
            chunk = read_json(chunk_path)
            local = RUN / "traces" / vid / chunk_path.name
            if local.exists():
                actual = read_json(local)
                for key in ("frame_indices", "frame_timestamps", "model_rgb_sha256"):
                    if actual[key] != chunk["trace"][key]:
                        raise ValueError(f"Input mismatch: {vid} {chunk_path.name} {key}")
                checked += len(actual["model_rgb_sha256"])
            for item in chunk["records"]:
                p, mode = extract_pyes({p["id"]: p["logprob"] for p in item["top20"]}, ids["Yes"], ids["No"])
                if p != item["pyes"] or mode != item["score_mode"]:
                    raise ValueError("Historical readout does not replay")
                values.append(p)
                old_modes[mode] += 1
                old_tokens += item["prompt_tokens"] + 1
        replay = segments_to_curve(values, media["segments"], row["duration"]).tolist()
        if replay != baseline["second_scores"]:
            raise ValueError("Historical full curve does not replay")
        if predictions[vid]["status"] == "complete" and checked != len(values):
            raise ValueError("Completed prediction missing matching source traces")
        baselines[vid] = metrics.two_second_scores(replay, int(row["duration"] / 2))
        old_values[vid] = values
        parity.append(
            dict(
                vid=vid,
                verified_new_windows=checked,
                baseline_windows=len(values),
                all_completed_new_inputs_match=True,
                baseline_readout_replayed=True,
            )
        )
    write_new(
        RUN / "runtime_input_parity.json",
        dict(
            status="passed",
            videos=parity,
            matched_windows=sum(x["verified_new_windows"] for x in parity),
            labels_read=False,
        ),
    )
    # Ground truth is accessed only after the prediction and source parity gates.
    if sha256(binding["annotation_path"]) != binding["annotation_sha256"]:
        raise ValueError("Pinned author annotation bytes changed")
    labels = read_json(binding["annotation_path"])
    details, new_valid, deltas = [], {}, []
    emitted = Counter()
    for row in rows:
        vid = row["vid"]
        old = metrics.video_metrics(baselines[vid], labels[vid]["anno"])
        prediction = predictions[vid]
        if prediction["status"] == "complete":
            new_valid[vid] = prediction["scores_2s"]
            new = metrics.video_metrics(prediction["scores_2s"], labels[vid]["anno"])
            delta = new["Top5_AP"] - old["Top5_AP"]
            new_top5 = new["top5_indices"]
        else:
            new, delta, new_top5 = None, -old["Top5_AP"], None
        values = [v for v in prediction["window_scores"] if v is not None]
        details.append(
            dict(
                vid=vid,
                status=prediction["status"],
                baseline=old,
                generic=new,
                delta_pp=delta,
                baseline_window_distribution=distribution(old_values[vid]),
                generic_window_distribution=distribution(values),
                old_top5=old["top5_indices"],
                new_top5=new_top5,
                unchanged_top5=new_top5 == old["top5_indices"],
                top5_intersection=None if new_top5 is None else len(set(new_top5) & set(old["top5_indices"])),
            )
        )
        deltas.append(delta)
        for path in (RUN / "requests" / vid).glob("*.result.json"):
            emitted[read_json(path)["generated_text"].strip()] += 1
    old_score = metrics.author_top5_map(baselines, labels)
    new_score = sum(0 if d["generic"] is None else d["generic"]["Top5_AP"] for d in details) / len(rows)
    if new_valid:
        official_new = metrics.author_top5_map(new_valid, labels)
        independent_valid = sum(d["generic"]["Top5_AP"] for d in details if d["generic"] is not None) / len(
            new_valid
        )
        if abs(official_new - independent_valid) > 0.00051:
            raise ValueError("Official new metric differs")
    if abs(old_score - sum(d["baseline"]["Top5_AP"] for d in details) / len(rows)) > 0.00051:
        raise ValueError("Official baseline metric differs")
    modes = Counter()
    for p in predictions.values():
        modes.update(p["score_modes"])
    result = dict(
        scope="official UMT val10, previously seen development videos",
        videos=manifest["videos"],
        denominator=len(rows),
        complete_videos=len(new_valid),
        baseline_Top5_mAP=old_score,
        generic_Top5_mAP=new_score,
        generic_minus_reze_pp=metrics.bootstrap_mean(deltas),
        improved=sum(d > 1e-10 for d in deltas),
        worsened=sum(d < -1e-10 for d in deltas),
        unchanged=sum(abs(d) <= 1e-10 for d in deltas),
        unchanged_top5=sum(d["unchanged_top5"] for d in details),
        generic_constant_videos=[
            d["vid"] for d in details if d["generic"] and d["generic"]["unique_scores"] == 1
        ],
        old_readout_modes=dict(old_modes),
        new_readout_modes=dict(modes),
        emitted_labels=dict(emitted),
        per_video=details,
        new_cost=freeze,
        gpu_lifecycle=read_json(RUN / "worker_exit.json"),
        cached_baseline_cost=dict(
            model_requests=sum(map(len, old_values.values())),
            token_count=old_tokens,
            new_requests_this_round=0,
            gpu_lifecycle_for_this_subset="not separable from old shared50-video workers",
        ),
        predictions_sha256=freeze["predictions_sha256"],
        annotation_sha256=binding["annotation_sha256"],
        comparison_script_sha256=sha256(Path(__file__)),
        runtime_input_parity_sha256=sha256(RUN / "runtime_input_parity.json"),
        no_new_model_calls_during_analysis=True,
        scientific_scope="Task-prompt package comparison; no independent five-dimension causal claim",
    )
    write_new(RUN / "comparison.json", result)
    target = Path(__file__).resolve().parent
    write_new(target / "comparison.json", result)
    with (target / "per_video.csv").open("x") as stream:
        writer = csv.writer(stream)
        writer.writerow(["vid", "status", "REZE_Top5_AP", "generic_Top5_AP", "delta_pp", "top5_intersection"])
        for d in details:
            writer.writerow(
                [
                    d["vid"],
                    d["status"],
                    d["baseline"]["Top5_AP"],
                    None if d["generic"] is None else d["generic"]["Top5_AP"],
                    d["delta_pp"],
                    d["top5_intersection"],
                ]
            )
    print(
        json.dumps(
            {
                k: result[k]
                for k in (
                    "denominator",
                    "complete_videos",
                    "baseline_Top5_mAP",
                    "generic_Top5_mAP",
                    "generic_minus_reze_pp",
                    "improved",
                    "worsened",
                    "unchanged",
                    "emitted_labels",
                )
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
