A,B=map(int,input().split())
C=str(input())
for i in range(B):
    D=str(input())
    a=0;b=0
    for j in range(len(D)):
        if C[a]==D[j]:a+=1
        if a==len(C):b=1;break
    if b==1:print('true')
    else:print('false')