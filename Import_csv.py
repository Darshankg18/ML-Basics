import pandas as pd

df=pd.read_csv("data.csv")
print(df)

# To print all the data in csv file
print(df.to_string())

print(pd.read_csv('data.csv',sep=';')) #Different Delimeter
print(pd.read_csv('data.csv',header=None)) #header=None tells Pandas that the CSV does not have a header row. The first row is treated as data, and Pandas assigns column numbers (0, 1, 2, ...).
print(pd.read_csv('data.csv',usecols=["Name","Type1"])) #Only certain columns
print(pd.read_csv('data.csv',index_col=0)) #Uses first column as index