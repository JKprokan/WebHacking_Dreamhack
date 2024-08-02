import hashlib
guestkey= hashlib.md5(b"guest").hexdigest()
adminkey=hashlib.md5("409ac0d96943d3da52f176ae9ff2b974".encode()).hexdigest()
print(adminkey)
#res="" #헛짓거리 해버림 우회할랬는데 우회문제아님
# moon=[99,97, 116, 32 ,102 ,108, 97 ,103, 46, 116, 120, 116] #cat flag.txt
# for i in moon:
#     res=res+chr(i)
# print(res)
# print(chr(99)+chr(97)+chr(116)+chr(32)+chr(102)+chr(108)+chr(97)+chr(103)+chr(46)+chr(116)+chr(120)+chr(116))