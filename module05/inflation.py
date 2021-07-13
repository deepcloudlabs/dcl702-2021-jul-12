import numpy as np
import pandas as pd

df = pd.read_csv("eurostat_hicpv2.csv")
eu_inflations = df.iloc[6:]
print(eu_inflations)
