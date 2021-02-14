a,b,c=map(int,input().split())
d=(a**2/(b**2+c**2))**0.5
print(int(b*d),int(c*d))