T=int(input())
for i in range(T):
    K=str(input())
    A=2015
    D=[0]*26
    for j in range(len(K)):
        D[int(ord(K[j]))-65]+=1
    for j in range(26):
        if D[j]>0:
            A-=j+65
    print(A)