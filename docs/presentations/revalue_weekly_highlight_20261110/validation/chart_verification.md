# Chart coordinate verification

Closed source: sources/slide_data.json and sources/progress.facts.json.
Classic bar axes explicitly declare minimum0 / maximum70 / major_unit20 in their SVG-local native payloads; visible major ticks are0/20/40/60. The final partial interval ends at70. Calculator invocations use the actual declared full scale0–70, not auto-normalization.

verify-charts: 03_memory_verifier.svg | object=memory-bars | type=bar | mode=direct-calc | scale=0-70 (explicit native axis, major ticks20) | calc=ran | svg=unchanged

verify-charts: 03_memory_verifier.svg | object=verifier-bars | type=bar | mode=direct-calc | scale=0-70 (explicit native axis, major ticks20) | calc=ran | svg=unchanged

verify-charts: 05_full50_results.svg | object=full50-bars | type=bar | mode=direct-calc | scale=0-70 (explicit native axis, major ticks20) | calc=ran | svg=unchanged

All bars use zero baseline. Category positions, widths and heights agree with the PowerPoint slot model and the given gap widths; precision of authored widths is0.0001px. Tables are semantic grids and do not enter this chart receipt.
