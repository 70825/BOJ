def check(x,y,z):
    try:
        for a in range(x,x+z):
            for b in range(y,y+z):
                if D[a][b]==0:return False
        return True
    except IndexError:return False
def add(x,y,z):
    for a in range(x,x+z):
        for b in range(y,y+z):
            D[a][b]=0
def erase(x,y,z):
    for a in range(x,x+z):
        for b in range(y,y+z):
            D[a][b]=1
def go(K,t,k):
    if t==0:
        global pp
        pp=min(pp,sum(K))
    if k==len(z):return
    if D[z[k][0]][z[k][1]]==0:go(K,t,k+1)
    for i in range(5,0,-1):
        if sum(K)<pp and K[i-1]<5 and check(z[k][0],z[k][1],i):
            add(z[k][0],z[k][1],i);K[i-1]+=1;go(K,t-i*i,k+1);K[i-1]-=1;erase(z[k][0],z[k][1],i)

D=[[*map(int,input().split())] for _ in range(10)]
ans=0
z=[]
pp=float('inf')
for i in range(10):
    for j in range(10):
        if D[i][j]==1:ans+=1;z+=[[i,j]]
go([0,0,0,0,0],ans,0)
print([pp,-1][pp==float('inf')])