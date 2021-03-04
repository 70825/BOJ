n,q=map(int,input().split())
D=[0]*(n+1)
for i in range(q):
    a,b,c=map(int,input().split())
    if a==1:D[b]+=c
    else:print(sum(D[b:c+1]))