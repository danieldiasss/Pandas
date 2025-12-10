#%%
import pandas as pd

df = pd.read_csv("../data/customers.csv" , sep=";")
df
# %%
df.dtypes

# %%
df["Points"].astype(str)

# %%

df["PointsDouble"] = df["Points"] * 2

# %%
df[["Points","PointsDouble"]].astype(float)

# %%
df[["UUID" , "Name"]].astype(int)
# %%

df["Lista"] = [[1,2] for i in df.index]
df
# %%
