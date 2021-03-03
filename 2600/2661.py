def check(t):
    if t==1:return True
    k=t//2
    for i in range(1,k+1):
        if D[t-i+1:t+1]==D[t-2*i+1:t-i+1]:return False
    return True

def go(t):
    if t==n+1:print(''.join(map(str,D[1::])));exit()
    for i in [1,2,3]:
        D[t]=i
        if check(t):go(t+1)
        D[t]=0
n=int(input())
D=[0]*(n+1)
go(1)