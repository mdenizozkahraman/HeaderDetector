import requests

def func_get_headers(url):

    response = requests.get(url)
    headers = response.headers

    print(headers)

func_get_headers("https://www.google.com")

