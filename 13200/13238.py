N=int(input())
D=[*map(int,input().split())]
ans=0
if len(D)!=0:
    for i in range(N-1):
        if ans<max(D[i+1::])-D[i]:ans=max(D[i+1::])-D[i]
print(ans)