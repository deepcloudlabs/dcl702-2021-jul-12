import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

countries_df = pd.read_json("countries.json")
countries_df.dropna(inplace=True)
countries_df.rename(columns={
    "_id": "code"
}, inplace=True)
countries_df.drop(columns=["cities", "localName", "capital"], inplace=True)

fig = plt.figure()
# plt.legend(loc="best")
# countries_df["lifeExpectancy"].plot()
sns.histplot(x='continent', data=countries_df)
fig.show()
