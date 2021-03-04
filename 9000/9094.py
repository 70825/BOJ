input=__import__('sys').stdin.readline
for i in range(int(input())):
    n,m=map(int,input().split())
    ans=0
    for j in range(1,n-1):
        for k in range(j+1,n):
            fx=(j**2+k**2+m)/(j*k)
            if fx==int(fx):ans+=1
    print(ans)