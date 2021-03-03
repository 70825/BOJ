n=int(input())
res=0
lo,hi=1,1
while 1:
    if hi**2-(hi-1)**2>n:break
    if hi**2-lo**2==n:
        print(hi);res+=1
    if hi**2-lo**2<=n:hi+=1
    else:lo+=1
if res==0:print(-1)