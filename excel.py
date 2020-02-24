import pandas as pd
data = pd.read_excel('xlsx.xlsx')
print (data)

print ("--------------------------------------------")

# Use the multi-axes indexing funtion
print (data.loc[[1,3,5],['salary','name']])

with pd.ExcelFile('xlsx.xlsx') as xls:
    df1 = pd.read_excel(xls, 'Sheet 1')
    df2 = pd.read_excel(xls, 'Sheet 2')

print("****Result Sheet 1****")
print(df1)
print("****Result Sheet 2****")
print(df2)