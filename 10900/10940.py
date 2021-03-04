import base64
K=str(base64.b16encode(str(input()).encode('utf-8')))
for i in range(2,len(K)-1):
    print(K[i],end="")