import requests

url="http://tmdals.duckdns.org:50017/"

for i in range(2,101):
    param={
        "page":i
    }
    res = requests.get(url,params=param)
    print(i)
    if "BUBU{" in res.text:
        print(res.text)
        print(i)
        break
    