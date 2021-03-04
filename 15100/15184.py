A=str(input()).upper()
D=[0]*26
for i in range(len(A)):
    if 0<=ord(A[i])-65<=25:
        D[ord(A[i])-65]+=1
for i in range(26):
    print(chr(i+65)+' | ',end="")
    for j in range(D[i]):print('*',end="")
    print("")