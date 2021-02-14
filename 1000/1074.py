n,r,c=map(int,input().split())
def Z(l,x,y):
    if l==1:return 1
    h=l>>1;k=h*h
    if x<h and y<h:return Z(h,x,y)
    elif x<h and y>=h:return k+Z(h,x,y-h)
    elif x>=h and y<h:return k*2+Z(h,x-h,y)
    return k*3+Z(h,x-h,y-h)
print(Z(1<<n,r,c)-1)