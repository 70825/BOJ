import sys
sys.setrecursionlimit(1000000)
input=__import__('sys').stdin.readline
def F(x):
    if S[x]<0:return x
    S[x]=F(S[x])
    return S[x]
def U(x,y):
    x,y=F(x),F(y)
    S[x]=y
while 1:
    m,n=map(int,input().split())
    if m==n==0:break
    S=[-1]*n
    D=[];ans=0;cnt=0
    for i in range(n):
        a,b,c=map(int,input().split())
        D.append([c,a,b])
    D.sort()
    for i in range(len(D)):ans+=D[i][0]
    for i in range(len(D)):
        if F(D[i][1])!=F(D[i][2]):
            U(D[i][1],D[i][2])
            ans-=D[i][0]
            if cnt==n-1:break
    print(ans)