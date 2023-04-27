import requests

url = "https://google.com"
if url.__contains__('http') and url.__contains__('://'):
    print("url looks valid")
    responce = requests.get(url, timeout = 10)
    print("getRequest status code = {}\nTimeout = {}".format(responce.status_code, 10))
else:
    print("check input url and try again")
