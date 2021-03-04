input=__import__('sys').stdin.readline
n,k=map(int,input().split())
D=[*map(int,input().split())]
pXor=[0]*(n+1)
for i in range(n):
    pXor[i+1]=pXor[i]^D[i]
ans=0
for i in range(k):
    s,e=map(int,input().split())
    z = pXor[e]^pXor[s-1]
    ans = ans ^ z
print(ans)