import pandas as pd
import plotly.express as px

df = pd.read_csv('../eurostat_hicpv2.csv')

value_vars = df.columns.tolist()[1:]

df = pd.melt(frame=df, id_vars='geo', value_vars=df.columns.tolist()[1:], var_name='years', value_name='inflation_rate')

df = df.iloc[6:]

fig = px.line(df, x="years", y="inflation_rate", color="geo", title='Inflation Rates Comparison')
fig.show()

df_geo = pd.json_normalize(pd.read_json('../covid19-stream-data.json')['records'])

df.loc[df.geo == 'United Kingdom', 'geo'] = 'United_Kingdom'
df.loc[df.geo == 'United States', 'geo'] = 'United_States'
df.loc[df.geo == 'North Macedonia', 'geo'] = 'North_Macedonia'

df_geo = pd.merge(df.reset_index(drop=True), df_geo, left_on='geo', right_on='countriesAndTerritories').drop(
    columns=['countriesAndTerritories'])

fig = px.choropleth(df_geo, locations="countryterritoryCode",
                    color="inflation_rate",
                    hover_name="geo",
                    animation_frame="years",
                    title="Yearly Inflation Rates",
                    color_continuous_scale="Sunsetdark",
                    projection='equirectangular')

fig.update_geos()
fig.update_layout(margin={'r': 0, 't': 50, 'l': 0, 'b': 0})
fig.show()
