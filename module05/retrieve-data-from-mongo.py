from pymongo import MongoClient
import numpy as np
import pandas as pd

client = MongoClient("mongodb://localhost:27017")

world_db = client['world']
countries = world_db.countries1

asian_countries = []
# http://binkurt.blogspot.com/2015/02/mongodb-ile-calsmak.html
for country in countries.find({"continent": "Asia"}):
    asian_countries.append(country)
    print(country)

df_asian = pd.DataFrame(asian_countries)
print(df_asian)
print(df_asian.columns)