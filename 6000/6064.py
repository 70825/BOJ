for _ in range(int(input())):
    m,n,x,y=map(int,input().split())
    x-=1;y-=1;z=x;ans=0
    while z<m*n:
        if z%n==y:print(z+1);ans=1;break
        z+=m
    if ans==0:print(-1)