a,b,c = map(int,input().split())
d = a*3600+b*60+c
s = int(input())
d += s
if d >= 86400:
    k = d // 86400
    d -= k*86400
h = d // 3600
m = (d-3600*h)//60
v = (d-3600*h-60*m)
print(h,m,v)