import sqlite3
import pandas as pd
#from sqlalchemy import create_engine


# connect to the database
conn = sqlite3.connect('population_data.db')

# # run a query
test = pd.read_sql('SELECT * FROM population_data', conn)
print(test)

test2 = pd.read_sql('SELECT * FROM population_data where Country_Code = "ABW" ', conn)
print(test2)

# engine = create_engine('sqlite:////home/workspace/3_sql_exercise/population_data.db')
# pd.read_sql("SELECT  * FROM population_data", engine)
# pd.read_sql("SELECT Country_Name, 1975 FROM population_data where Country_Name = 'Aruba'", engine)