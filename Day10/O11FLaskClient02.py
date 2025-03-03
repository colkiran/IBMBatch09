import json

import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + 'getproduct/thumbs_up')

res = response.json()

print(res)

print("put".center(60, "-"))

response = requests.put(BASE + 'getproduct/coke', data={'cat': 'beverage'})
res = response.json()

print(f"res :{res}")

print("Patch".center(60, "-"))

data = {'price': 5000}

response = requests.patch(BASE + "getproduct/coke", json = json.dumps(data))

res = response.json()
print(res)
print("post".center(60, "-"))
fanta = {'item': '200 ml Bottel', 'price': 20, 'qty': '250'}

response = requests.post(BASE + "getproduct/fanta", json = json.dumps(fanta))
res  = response.json()

for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 60)

print("delete".center(60, "-"))

response = requests.delete(BASE + "getproduct/thumbs_up")
res = response.json()

for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 60)
