import pandas as pd
df=pd.read_csv("data.csv",index_col=0)
print(df.mean(numeric_only=True)) #Mean of all numeric coloumn
print(df.sum(numeric_only=True)) #Sum of all numeric coloumn
print(df.min(numeric_only=True)) #Minimum value of all numeric coloumn
print(df.max(numeric_only=True)) #Maximum value of all numeric coloumn
print(df.count()) #Count of all coloumn
print(df["Height"].agg(['mean','max','min','sum'])) #Single Coloumn aggreagte function
# Group the DataFrame based on the "Type1" column
group = df.groupby("Type1")
# Loop through each group
# name = the Type1 value (e.g., Fire, Water, Grass)
# data = all rows belonging to that Type1 group
for name, data in group:
    # Print the group name
    print(name)

    # Print all Pokémon belonging to that group
    print(data)