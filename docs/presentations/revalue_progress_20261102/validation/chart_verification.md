# Chart verification

Based on the three keyed chart objects in design_spec.md §IX. The calculator used explicit native category slots and the same value ranges as the final SVG.

verify-charts: 05_main_results.svg | object=recall-bars | type=bar | mode=direct-calc | scale=0–40 (from ticks) | calc=ran | svg=unchanged

verify-charts: 06_contract_repair.svg | object=invalid-bars | type=column | mode=direct-calc | scale=0–30 (from ticks) | calc=ran | svg=unchanged

verify-charts: 07_verdict_distribution.svg | object=verdict-stacks | type=stacked-bar | mode=decomposable-calc | scale=0–139 (from ticks) | calc=ran×4 for cumulative boundaries | svg=unchanged

The recall bars measure 98.84 and 131.74px, using 560px / 40. The invalid-output columns measure 230 and 50px, using 300px / 30. Stacked counts use 7px per candidate: Q cumulative widths 490, 903, 952, 973; Q+V cumulative widths 441, 889, 959, 973. Segment widths and starts equal adjacent cumulative differences. Per-category totals are exactly 139.

# Carrier-receipt review

Final checker: 12 pages passed, 0 errors, 0 warnings; 3 native charts, 2 native tables, 2 helper-authored presets, 6 line-end markers and 2 inline emphasis runs.

The chart/table jobs are carried by the 5 named data objects. The input and candidate output in the pipeline use actual flowchart input/output and document presets. Straight edges carry the input flow, evidence support and added dependency; no solid-arrow silhouette is required for those thin relations. Discrete counts use common scales, while the coverage example explicitly states that its geometry has no real temporal proportion.

No separate carrier-and-field preset contour is needed: shared planes distinguish frozen inputs and response excerpts, table cells own metrics, and matching axes own quantities. Snipped corners or enclosing badges would introduce an additional status boundary that these units do not possess. Grouping and ownership are already carried by the bounded inputs, response fields and candidate frames. Emphasis is carried by source-backed numerals, weight and explicit labels rather than an annotation emblem.

Gradients are absent because each data category represents a discrete state with an explicit label, and no continuous uncertainty scale is being encoded. Filters are absent because no overlapping or floating layer has a depth relationship to communicate. No image or icon pool was prepared. Cases are descriptions of saved responses, not synthetic pictures presented as visual evidence.

The first live-preview launch failed with missing Flask. Native export also needed python-pptx. Document-tool dependencies were installed into the isolated directory `$WORKSPACE_PARENT/.cache/codex/ppt-master-runtime/packages`, accessed only through command-scoped PYTHONPATH. No experiment environment or inference process was changed. Export then passed, and live preview started at http://127.0.0.1:6060; automatic browser opening was unavailable. SVG source, final checker and native PPTX postflight are the delivery checks; no per-page rendered visual-review pass is claimed.
