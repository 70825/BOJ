r,c=map(int,input().split())
D=[];S=[0]*10;t=1
for i in range(r):D.append(input())
for i in range(c-1,-1,-1):
    ans=0
    for j in range(r):
        if 48<ord(D[j][i])<58 and S[int(D[j][i])]==0:
            S[int(D[j][i])]=t;ans+=1
    if ans!=0:t+=1
for i in range(1,10):print(S[i])