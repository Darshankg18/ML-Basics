import pandas as pd
data=[10,20,30]
series=pd.Series(data)
## For custom index
series1=pd.Series(data,index=['a','b','c'])
print(series)
print(series1)
## To access elements in series
## For custom index
print(series1.loc['a'])
## For Normal index
print(series.iloc[1])