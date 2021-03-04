n,m=map(int,input().split())
memo1=[];memo2=[];k=0;ans=0
for i in range(n):
    memo1.append([*map(str,input().split())])
for i in range(m):
    p=[]
    for j in range(n):
        p.append(memo1[j][i])
    memo2.append(p)
for i in range(n):
    s=0
    for j in range(m):
        s+=memo1[i][j].count('9')
    ans+=s
    k=max(k,s)
for i in range(m):
    s=0
    for j in range(n):
        s+=memo2[i][j].count('9')
    k=max(k,s)
print(ans-k)