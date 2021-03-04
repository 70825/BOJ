n,X=map(int,input().split())
D=sorted([*map(int,input().split())])
ans=1
if len(D)==1:print(1)
else:
    for i in range(n-1):
        if D[i]+D[i+1]<=X:ans+=1
        else:break
    print(ans)