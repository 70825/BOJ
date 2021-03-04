N,W,H=map(int,input().split())
for i in range(N):
    A=int(input())
    if A<=(W**2+H**2)**0.5:print('YES')
    else:print('NO')