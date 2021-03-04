import hashlib
a=hashlib.new('sha')
a.update(str(input()).encode())
print(a.hexdigest())