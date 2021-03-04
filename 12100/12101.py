def go(n,now=0,D=[]):
    global ans
    if now>=n:
        if now==n:ans+=1
        if ans==k:print('+'.join(map(str,D)));exit()
        return
    for x in [1,2,3]:
        go(n,now+x,D+[x])
ans=0
n,k=map(int,input().split())
go(n)
print(-1)