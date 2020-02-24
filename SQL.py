from sqlalchemy import create_engine
import pandas as pd
from pandas.io import sql

data = pd.read_csv('csv.csv')

# Create the db engine
engine = create_engine('sqlite:///:memory:')

# Store the dataframe as a table
data.to_sql('data_table', engine)

# Query 1 on the relational table
res1 = pd.read_sql_query('SELECT * FROM data_table', engine)
print('Result 1')
print(res1)
print('')

# Query 2 on the relational table
res2 = pd.read_sql_query('SELECT dept, sum(salary) FROM data_table group by dept', engine)
print('Result 2')
print(res2)

print('----------------------------')

# Insert another row
sql.execute('INSERT INTO data_table VALUES(?,?,?,?,?,?)', engine, params=[('id',9,'Ruby',711.20,'2015-03-27','IT')])

# Read from the relational table
res = pd.read_sql_query('SELECT ID,Dept,Name,Salary,start_date FROM data_table', engine)
print(res)

print('----------------------------')

sql.execute('Delete from data_table where name = (?) ', engine,  params=[('Gary')])

res = pd.read_sql_query('SELECT ID,Dept,Name,Salary,start_date FROM data_table', engine)
print(res)