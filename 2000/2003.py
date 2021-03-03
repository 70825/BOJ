input=__import__('sys').stdin.readline
n,m=map(int,input().split())
D=[*map(int,input().split())]
res,Sum,lo,hi=0,0,0,0
while 1:
    if Sum >= m: Sum-=D[lo]; lo+=1
    elif hi==n:break
    else:Sum+=D[hi]; hi+=1;
    if Sum==m:res+=1
print(res)