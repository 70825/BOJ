T=int(input())
for i in range(T):
    N=int(input())
    A=str(input())
    B=str(input())
    w=0;b=0;k=0
    for j in range(N):
        if A[j]!=B[j]:
            if A[j]=='W':w+=1
            elif A[j]=='B':b+=1
    if w>0 and b>0:
        while w!=0 and b!=0:w-=1;b-=1;k+=1
    if w>0:
        while w!=0:w-=1;k+=1
    if b>0:
        while b!=0:b-=1;k+=1
    print(k)