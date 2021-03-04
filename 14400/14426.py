from bisect import bisect
input=lambda:__import__('sys').stdin.readline().strip()
n,m=map(int,input().split())
D=sorted([input() for i in range(n)])
ans=0
for i in range(m):
    s=input()
    k=bisect(D,s)
    if (k>0 and D[k-1][:len(s)]==s) or (k<n and D[k][:len(s)]==s):ans+=1
print(ans)