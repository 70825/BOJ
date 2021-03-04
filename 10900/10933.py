import hashlib
a=hashlib.new('ripemd160')
a.update(str(input()).encode())
print(a.hexdigest())