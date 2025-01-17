import requests
from pprint import pp
import json

Base_url = "https://icanhazdadjoke.com/"
API_PAGE = ""

URL = Base_url + API_PAGE

header_dict = {
    "Accept": "application/json"
}

response = requests.get(URL,headers=header_dict)
print(response.status_code)
print(response.text)
print(type(response.text))

json_respons = json.loads(response.text)
print(type(json_respons))
pp(json_respons)


with open("joke.txt","w") as file_handler:
    file_handler.write(response.text)
