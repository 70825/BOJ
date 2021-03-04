import base64
def stringToBase64(s):
    return base64.b64encode(s.encode('utf-8'))
K=str(stringToBase64(str(input())))
for i in range(2,len(K)-1):
    print(K[i],end="")