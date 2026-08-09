import pandas as pd 

df = pd.read_csv("data.csv")

# Height >= 2
tall = df[df["Height"] >= 2]

# Weight >= 100
heavy = df[df["Weight"] >= 100]

# Legendary Pokémon
legendary = df[df["Legendary"] == 1]

# Fire AND Flying
ff_pokemon = df[
    (df["Type1"] == "Fire") &
    (df["Type2"] == "Flying")
]

# Names containing "AI"
v = df[df["Name"].str.contains("AI", case=False)]

# Names starting with "A"
b = df[df["Name"].str.startswith("A")]

print(tall)
print(v)
print(b)
print(ff_pokemon)
print(legendary)
print(heavy)