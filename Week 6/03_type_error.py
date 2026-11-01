# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

import pandas as pd

df = pd.DataFrame({"value": ["87", "120", "45"], "limit": [100, 100, 100]}) #value are stored as text 
df["value"] = df["value"].astype(float) #conversion has been made to float.
df["percent"] = (df["value"] / df["limit"]) * 100
print(df)