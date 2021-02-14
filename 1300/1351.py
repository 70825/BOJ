def go(a,b,c):
    if a in D:return D[a]
    else:
        D[a]=go(a//b,b,c)+go(a//c,b,c)
        return D[a]
n,p,q=map(int,input().split())
D=dict();D[0]=1
print(go(n,p,q))