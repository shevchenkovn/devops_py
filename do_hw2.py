import requests
result =[] ## !=200 response status code urls
urls = [
    "https://google.com",
    "https://www.mcdonalds.com/ru/",
    "https://www.kfc-ukraine.com/ru/"
    ]

for url in urls:
    if url.__contains__('http') and url.__contains__('://'):
        print("url looks valid")
        responce = requests.get(url, timeout = 10)
        if responce.status_code != 200:
            result.append(url)

        print("getRequest status code = {}\nTimeout = {}".format(responce.status_code, 10))
    else:
        print("check input url and try again")


print("Urls that didnt gave 200 status code:")
print(result)
