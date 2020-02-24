import pandas as pd

#read json
data = pd.read_json('json.json')
#read json
print (data)

print ("---------------------------------------------")

# Use the multi-axes indexing funtion
print (data.loc[[1,3,5],['Salary','Name']])

print ("---------------------------------------------")

print(data.to_json(orient='records', lines=True))
