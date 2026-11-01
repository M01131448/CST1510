# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

import pandas as pd

df = pd.DataFrame({
    "label": ["R-001", "R-002", "R-003"],
    "value": [87, 120,45] #a value was missing in the Array, in a DataFrame, every column must have equal rows.
})
