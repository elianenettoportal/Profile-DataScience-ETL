import requests as req
import json
import pandas as pd

url = 'http://api.worldbank.org/v2/countries/br;cn;us;de/indicators/SP.POP.TOTL/?format=json&per_page=1000'
print(url)
data = req.get(url)
# print(data.json())

df = pd.DataFrame(data.json()[1])

# ------------------------------------------------------
# TODO: get the url ready
url2 = 'http://api.worldbank.org/v2/indicator/SP.RUR.TOTL?end=2001&locations=AU&start=1995&format=json'
data2 = req.get(url2)
# print(data2.json())

df2 = pd.DataFrame(data.json()[1])


print(df)
print(df2)
