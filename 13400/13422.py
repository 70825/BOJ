input=__import__('sys').stdin.readline
for _ in range(int(input())):
    n,m,k=map(int,input().split())
    D=[*map(int,input().split())]
    res,Sum,lo,hi=0,0,0,0
    if n==m:
        if sum(D)<k:print(1)
        else:print(0)
        continue
    for i in range(n+m):
        if hi<m:Sum+=D[hi];hi+=1
        else:
            if Sum<k:res+=1
            Sum-=D[lo];lo+=1
            Sum+=D[hi%n];hi+=1
    print(res)