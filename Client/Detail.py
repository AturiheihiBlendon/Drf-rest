import requests

url = "http://127.0.0.1:8000/products/1"

response = requests.get(url)
print(response.text)
print("-------------------------------------------------------------")
todict = response.json()
print(todict)