s="1_c_3_c_0__ff_3e"
ans=0
cnt=15
for i in s:
    if i == "_":
        res=0xb
    elif(i in ["c","d","e","f"]):
        res=int(i,base=16)
    else:
        res=int(i)
    ans=(res << (cnt*4)) | ans
    cnt-=1
print(ans)