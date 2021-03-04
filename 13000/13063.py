while 1:
    a,b,c=map(int,input().split())
    if a==b==c==0:break
    d=a-b-c
    if b+d<a//2+1:print(-1)
    else:
        k=0
        while b+k<a//2+1:k+=1
        print(k)