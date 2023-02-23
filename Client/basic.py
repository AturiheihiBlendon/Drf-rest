import requests

# endpoint URL

# baseURL = "http://httpbin.org/anything"

# response = requests.get(baseURL)
# print(response.text)
# print(type(response.text))

# print("-------------------------------------------------------------")
# print("-------------------------------------------------------------")
# print("-------------------------------------------------------------")
# print("-------------------------------------------------------------")

# todict = response.json()
# print(todict)
# print(type(todict))


url = "http://127.0.0.1:8000/api/"

response = requests.get(url, json={"name": "Blendon", "age":23})
print(response.text)
print("-------------------------------------------------------------")
todict = response.json()
print(todict)