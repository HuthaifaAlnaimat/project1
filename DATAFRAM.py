import pandas as pd

df=pd.read_csv('Car data.csv')
print(df.columns)
print(df["Car_Name"].head())
print(df.tail())
print(df.loc[0])
dic={
    "colum1":[10, 20,300],
    "colum2":[30, 10,100]

}
df2=pd.DataFrame(dic)
print(df2.head(2))
print(df.shape)

#df #data farme