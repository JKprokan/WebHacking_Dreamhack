# a="\'=\'"
# for i in a:
#     print(ord(i))
from hashlib import md5

for i in range(10000000):
    raw_md5=md5(str(i).encode("ascii")).digest()
    if (b'\x27\x3d\x27' in raw_md5):
        print(i, raw_md5)