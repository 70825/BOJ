input=__import__('sys').stdin.readline
n,s=map(int,input().split())
D=[*map(int,input().split())]
res,Sum,lo,hi=0,0,0,0
ans=float('inf')
while 1:
    if Sum>=s: Sum-=D[lo]; lo+=1
    elif hi==len(D):break
    else:Sum+=D[hi]; hi+=1;
    if Sum>=s:ans=min(ans,hi-lo)
print([ans,0][ans==float('inf')])