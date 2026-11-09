# Chart coordinate verification

Three chart objects declared in Design Spec IX, three scoped plot-area markers verified. Calculator runs used the explicitly drawn zero-based axis ranges.

- verify-charts: 05_full50.svg | object=early-results | type=grouped-column | mode=decomposable-calc | scale=0–80 from ticks | calc=ran×3 | svg=updated category alignment. Values map to height=value×300/80; all six heights agree within 0.0001px. Category slot centers are 280 and 620; each cluster uses three independent 62px bars at offsets −104, −31, +42. This categorical spacing is checked separately from the calculator's single-series packing.
- verify-charts: 06_memory40.svg | object=dense-results | type=bar | mode=direct-calc | scale=0–70 from ticks | calc=ran | svg=updated vertical placement by −2px. Width=value×840/70. Six 55px category slots, 28px bars, equivalent gap_width=96.428571%. Widths and slot centers match.
- verify-charts: 08_verifier_map.svg | object=verifier-map | type=bar | mode=direct-calc | scale=0–70 from ticks | calc=ran | svg=unchanged. Width=value×840/70. Four 80px slots, 36px bars, equivalent gap_width=122.222222%. All widths and slot centers match.

Charts retain four-decimal original metrics in native metadata; visible point labels use 0.00 formatting. No axis is cropped to exaggerate small changes. Tables have no quantitative geometry and are not counted as chart objects.
