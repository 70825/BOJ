X,Y,N=map(int,input().split())
for i in range(N):
    s=''
    if (i+1)%X==0:
        s+='Fizz'
    if (i+1)%Y==0:
        s+='Buzz'
    if len(s)==0:print(i+1)
    else:print(s)