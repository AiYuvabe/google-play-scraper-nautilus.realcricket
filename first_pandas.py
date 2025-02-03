import pandas as pd


df =pd.read_csv("world_population.csv")
# print(type(df.to_string()))
# print(type(df))

# print(df)
# print(df.head(10))

# print(df.tail(5))
# print(df.iloc[50])
# print(df.iloc[10:20])
# print(df.loc[10:20])
# print(df[["Country","Capital"]])
# print(df.iloc[10:20])
asian_country=df[df["Continent"]=="Asia"]
# print(df[df["Continent"]=="Asia"])

print(asian_country)
# print(df[df["Area"] == df["Area"].max()])
# print(asian_country["Area"]==df["Area"].max())
# print(df[df["Area"] == df["Area"].min()])
# print(df[df["Capital"] == df["Capital"].max()])
# print(df[df["Area"] == df["Area"].max()])
# print(df.iloc[1,2])

print(df.loc[df["Continent"] == "Asia","Area"].max())