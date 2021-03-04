def go(day,s):
    global ans
    if day == n:
        ans=max(ans,s)
        return
    if day>n:return
    go(day+1,s)
    go(day+a[day],s+b[day])
a=[];b=[]
n=int(input())
for i in range(n):
    X,Y=map(int,input().split())
    a.append(X);b.append(Y)
ans=0
go(0,0)
print(ans)