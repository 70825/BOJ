input=__import__('sys').stdin.readline
n,m=map(int,input().split())
D=sorted([int(input()) for i in range(n)])
res=float('inf')
i,j=0,0
while i<n and j<n:
    if D[j]-D[i]>=m:
        res=min(res,D[j]-D[i])
        i+=1
    else:j+=1
print(res)