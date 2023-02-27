import requests

url = "http://127.0.0.1:8000/products/"
data = {
    "title": "Pencil"
}

response = requests.post(url, data=data)
print(response.text)
print("-------------------------------------------------------------")
todict = response.json()
print(todict)