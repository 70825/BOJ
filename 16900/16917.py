a,b,c,x,y=map(int,input().split())
if 2*c<=a+b:
    if min(x,y)==x:ans=(2*x*c+b*(y-x))
    else:ans=(2*y*c+a*(x-y))
else:ans=(a*x+y*b)
print(min(ans,max(x,y)*2*c))