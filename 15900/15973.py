a,b,c,d=map(int,input().split())
w,x,y,z=map(int,input().split())
if (c,d)==(w,x) or (a,b)==(y,z) or (c,b)==(w,z) or (a,d)==(y,x):
    print('POINT')
elif (w==c or a==y) and ((x<=d<=z and x<=b<=z) or (b<=x<=d and b<=z<=d) or (x<=b and b<=z<=d) or (b<=x and x<=d<=z)):
    print('LINE')
elif (d==x or b==z) and ((w<=a<=y and w<=c<=y) or (a<=w<=c and a<=y<=c) or (w<=a and a<=y<=c) or (a<=w and w<=c<=y)):
    print('LINE')
elif a<=w and c>=y and b<=x and d>=z:
    print('FACE')
elif w<=a and y>=c and x<=b and z>=d:
    print('FACE')
elif ((a<=w and c>w) or (w<=a<y and c>y)) and ((b<=x and d>x) or (x<=b<z)):
    print('FACE')
elif ((w<=a and y>a) or (a<=w<c and y>c)) and ((x<=b and z>b) or (b<=x<d)):
    print('FACE')
else:print('NULL')