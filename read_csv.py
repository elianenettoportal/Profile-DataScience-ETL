import pandas as pd
import csv
from itertools import islice
from operator import itemgetter

get_columns = itemgetter('Country Name','Country Code','Indicator Name','Indicator Code')
# with open('population_data.csv') as csvfile:
#     reader = csv.DictReader(csvfile)
    # for row in islice(reader, 10): # first 10 only
    #     print(row)

df_population = pd.read_csv('population_data.csv', skiprows=4)
column_missing_values = df_population.isnull().sum()
row_missing_values = df_population.isnull().sum(axis=1)
df = df_population

df_population = df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
column_missing_valuesd = df.isnull().sum()
df[df.isnull().any(axis=1)]


print(df)