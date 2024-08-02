import requests

url="http://tmdals.duckdns.org:50017/?page="

for i in (2,range(101)):
    res = requests.get(url+str(i))
    print(i)
    if "BUBU{" in res.text:
        print(res.text)
        print(i)
        break
    