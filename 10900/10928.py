import hashlib
a=input()
b=a.encode()
m=hashlib.sha1()
m.update(b)
print(m.hexdigest())