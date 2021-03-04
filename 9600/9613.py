def gcd(a,b):
    if b==0:return a
    return gcd(b,a%b)
for i in range(int(input())):
    ans=0
    D=[*map(int,input().split())]
    N=D[0];D.pop(0)
    D.sort()
    for j in range(N-1):
        for k in range(j+1,N):
            ans+=gcd(D[k],D[j])
    print(ans)