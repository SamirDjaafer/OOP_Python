import requests

path = "https://github.com/Filipe-p/eng57-JSON-API-Postocodes/blob/master/"
arguments = "get_request_postcodes.py"

url_target = path + arguments

response = requests.get(url_target)

print(response.json())


