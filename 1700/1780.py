def go(t,x,y):
    flag = True
    val = -2
    for i in range(x,x+t):
        for j in range(y,y+t):
            if val == -2:val = D[i][j]
            elif val != D[i][j]: flag = False
    if flag: ans[val]+=1
    else:
        t //= 3
        for i in range(3):
            for j in range(3):
                go(t,x+t*i,y+t*j)
input=__import__('sys').stdin.readline
n = int(input())
ans = [0,0,0] #0,1,-1
D = [[*map(int,input().split())] for _ in range(n)]
go(n,0,0)
print("{}\n{}\n{}\n".format(ans[-1],ans[0],ans[1]))