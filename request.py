import requests
cookie = {}
for i in range(1,101,1):
    cookie[str(i)] = str(i)
#requests.get(url, params= dictionary_of_get)
#requests.post(url=,data=)
#requests.get(url, headers=dictionary_of_headers, cookies=dictionary_of_cookies)
result = requests.get('http://kslweb1.spb.ctf.su/first/level7/', cookies = cookie)
print(result.text)