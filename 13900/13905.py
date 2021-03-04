import sys
sys.setrecursionlimit(100000)
input=__import__('sys').stdin.readline
def F(x):
    if S[x]==x:return x
    S[x]=F(S[x])
    return S[x]
n,m=map(int,input().split())
s,e=map(int,input().split())
S=[i for i in range(n+1)]
D=[]
for i in range(m):
    a,b,c=map(int,input().split())
    D.append((c,a,b))
D.sort(reverse=True)
for i in range(m):
    if F(D[i][1])!=F(D[i][2]):
        S[F(D[i][1])]=F(D[i][2])
        if S[e]!=-1 and S[F(e)]==S[F(s)]:
            print(D[i][0]);exit()
print(0)