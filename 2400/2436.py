a,b = map(int,input().split())
c = a * b
ans = [-1,-1,float('inf')]
for x in range(a, b+1, a):
    y = c//x
    if x > y: break
    e,f = y,x
    while f!=0:e,f=f,e%f
    if e != a or x*y != c: continue
    if ans[2] > x + y:ans = [x,y,x+y]
print(ans[0],ans[1])