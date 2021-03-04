A,B=map(int,input().split());k=0
T=int(input());z=[0]*T;x=[0]*T;y=[0]*T
for i in range(T):
    X,Y=map(int,input().split())
    z[i]=abs(A-X)+abs(B-Y)
    x[i]=X;y[i]=Y
for i in range(T):
    if min(z)==abs(A-x[i])+abs(B-y[i]):
        k=i
print(x[k],y[k])