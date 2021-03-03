def cross(x1, y1, x2, y2):
    return x1*y2 - x2*y1
n=int(input())
D=[[*map(int,input().split())] for _ in range(n)]
x1,y1=D[0]
ans=0
for i in range(1,n-1):
    x2,y2=D[i]
    x3,y3=D[i+1]
    ans+=cross(x2-x1,y2-y1,x3-x1,y3-y1)
print(round(abs(ans)/2,1))