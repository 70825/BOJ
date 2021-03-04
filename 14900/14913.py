a,d,k=map(int,input().split())
k-=a
if k/d!=int(k/d) or k*d<0:print('X')
else:print(int(k/d)+1)