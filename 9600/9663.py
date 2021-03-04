def go(t):
    global ans
    if t==n:ans+=1;return
    for i in range(n):
        if vertical[i]==right[n-1+i-t]==left[t+i]==0:
            vertical[i],right[n-1+i-t],left[t+i]=1,1,1
            go(t+1)
            vertical[i],right[n-1+i-t],left[t+i]=0,0,0
n=int(input())
vertical=[0]*n
right=[0]*(2*n-1)
left=[0]*(2*n-1)
ans=0
go(0)
print(ans)