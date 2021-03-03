def go(t,x,y):
    flag = [True,D[x][y]]
    for i in range(x,x+t):
        for j in range(y,y+t):
            if flag[1]!=D[i][j]:flag[0] = False
    if flag[0]: ans[flag[1]]+=1
    else:
        t//=2
        go(t,x,y)
        go(t,x+t,y)
        go(t,x,y+t)
        go(t,x+t,y+t)

n = int(input())
D = [[*map(int,input().split())] for _ in range(n)]
ans = [0,0]
go(n,0,0)
print('{}\n{}'.format(ans[0],ans[1]))