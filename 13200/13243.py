N=int(input())
D=[*map(int,input().split())]
Max,Len=0,0
ans,k=0,0
for i in range(N):
    if i==0:
        Max=ans=D[0]
        Len=k=1
    else:
        if D[i-1]<=D[i]:ans+=D[i];k+=1
        else:
            if k>Len:Max=ans;Len=k
            ans=D[i];k=1
if k>Len:Max=ans;Len=k
print(Len,Max)