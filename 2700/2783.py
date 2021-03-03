X,Y=map(int,input().split())
c=1000/Y;Y=X*c
for i in range(int(input())):
    a,b=map(int,input().split())
    c=1000/b;d=a*c
    if Y>d:Y=d
print(Y)