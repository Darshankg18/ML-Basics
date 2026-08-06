import pandas as pd
Data={"Name":["Captain America","IronMan","Black Panther"],
      "Age":[27,29,28]}
df=pd.DataFrame(Data,index=[1,2,3])


## Accessing elements
print(df.loc[1])
print(df.iloc[1])
## Adding new column
df["Job"]=["cook","N/A","Cashier"]
## Adding new row
new_row=pd.DataFrame([{"Name":"Thor","Age":20,"Job":"MD"}],index=[4])
## Concatanation of new row
df=pd.concat([df,new_row])
print(df)

##Common operations
df.shape
df.columns
df["Age"]
df[["Name","Age"]]
df.iloc[0]
df.loc[1]
df.describe()