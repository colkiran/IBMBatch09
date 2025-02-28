
"""
1. load  - is used to read the document from a file
2. loads - is used to convert JSON string to Python dictionary
"""

import json

JFR = open("books.json", "r")
jsonFile = json.load(JFR)

# print(jsonFile)
for book in jsonFile['books']:
    print(book['name'])
    print("-" * len(book['name']))
    for k, v in book.items():
        print(k, "=>", v)
    print("-" * 60)

print("loads".center(60, "-"))
empdata = '{"name": "Kevin", "age": 32, "city": "Los Angels"}'
print(empdata)
print(type(empdata))

print("-" * 60)
# convert the string into a python dictionary
res = json.loads(empdata)
print(res)
print(type(res))

print("-" * 60)
for k in res.keys():
    print(k, "=>", res[k])
