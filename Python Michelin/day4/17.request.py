import requests
Base_url = "https://icanhazdadjoke.com/"
API_PAGE = "/api"

URL = Base_url + API_PAGE

response = requests.get(URL)
print(response.status_code)
print(response.text)

file_handler = open("joke.html","w")
file_handler.write(response.text)
file_handler.close()