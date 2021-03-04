input=__import__('sys').stdin.readline
n,m=map(int,input().split())
D=[0]*(n+1)
for i in range(m):
    a,b=map(int,input().split())
    D[a]+=1;D[b]+=1
print('\n'.join(map(str,D[1::])))