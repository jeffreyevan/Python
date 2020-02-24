import pandas as pd

#read csv
data = pd.read_csv('csv.csv')
#print csv
print (data)

print ("---------------------------------------------")

# Slice the result for first 5 rows
print (data[0:5]['salary'])

print ("---------------------------------------------")

# Use the multi-axes indexing funtion
print (data.loc[:,['salary','name']])

print ("---------------------------------------------")

# Use the multi-axes indexing funtion
print (data.loc[[1,3,5],['salary','name']])

print ("---------------------------------------------")

# Use the multi-axes indexing funtion
print (data.loc[2:6,['salary','name']])