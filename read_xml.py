import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import pandas as pd

# --------------------------------------- EXAMPLE 1

tree = ET.parse('books.xml')
root = tree.getroot()

data =[]
cols =['Title', 'Author', 'Genre', 'Price', 'Description' ]
for book in root.iter('book'):
    item=[]
    item.append(book.find('title').text)
    item.append(book.find('author').text)
    item.append(book.find('genre').text)
    item.append(book.find('price').text)
    item.append(book.find('description').text)
    data.append(item)

print(data)
df = pd.DataFrame(data)
df.columns =cols
print(df)

# ---------------------------------------EXAMPLE 2
# tree = ET.parse('population_data_short.xml')
# root = tree.getroot()

# data =[]
# cols =['Country or Area', 'Year', 'Item', 'Value']
# for i, child in enumerate(root[0]):
#     data.append([subchild.text for subchild in child])

# df = pd.DataFrame(data)
# df.columns = cols
# print(df)

# --------------------------------------- EXAMPLE 3
# with open("population_data_short.xml") as fp:
#     soup = BeautifulSoup(fp, "lxml")

# # i = 0
# # for record in soup.find_all('record'):
# #     i += 1
# #     for record in record.find_all('field'):
# #         print(record['name'], ': ' , record.text)
# #     print()
# #     if i == 5:
# #         break

# data_dictionary = {'Country or Area':[], 'Year':[], 'Item':[], 'Value':[]}
# for record in soup.find_all('record'):
#     for record in record.find_all('field'):
#         data_dictionary[record['name']].append(record.text)


# df = pd.DataFrame.from_dict(data_dictionary)
# df = df.pivot(index='Country or Area', columns='Year', values='Value')
# df.reset_index(level=0, inplace=True)

# print(df)
    



