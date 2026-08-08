import pandas as pd 

# Read the CSV file and use the "Name" column as the DataFrame index
df = pd.read_csv('data.csv', index_col="Name")

# Print the "Name" column
# ❌ Won't work because "Name" is now the index if we remove that then it will work
print(df["Name"])

# Print the "Name" and "Weight" columns
print(df[["Name", "Weight"]])

# Print the entire DataFrame without truncating the output
print(df.to_string())

# Select and print the complete row for the Pokémon "Pikachu"
print(df.loc["Pikachu"])


# Select the "Height" and "Weight" of Charizard
print(df.loc["Charizard", ["Height", "Weight"]])

# Select rows from Charizard to Blastoise
# and display only the Height and Weight columns
print(df.loc["Charizard":"Blastoise", ["Height", "Weight"]])

# Select rows from position 0 to position 10
# (11 is excluded)
print(df.iloc[0:11])

# Select rows 0 to 10 with a step of 2
# and select columns 0 to 2
# (column position 3 is excluded)
print(df.iloc[0:11:2, 0:3])


# Ask the user to enter a Pokémon name
pokemon = input("Enter a pokemon name:")

try:
    # Find and print the row corresponding to the entered Pokémon
    print(df.loc[pokemon])

except KeyError:
    # Runs when the entered Pokémon name is not found in the index
    print(f"{pokemon} not registered")