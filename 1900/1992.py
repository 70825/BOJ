def same(t,x,y):
    flag = True
    val = ''
    for i in range(x,x+t):
        for j in range(y,y+t):
            if val == '':val = D[i][j]
            elif val != D[i][j]:flag = False
    return flag,val
def go(t,x,y):
    r_flag = [[True,-1] for _ in range(4)]
    for idx,[nx,ny] in enumerate([[x,y],[x,y+t],[x+t,y],[x+t,y+t]]):
        flag, val = same(t,nx,ny)
        if flag:r_flag[idx][1] = val
        else:r_flag[idx][0] = False
    if min(r_flag[i][0] for i in range(4)) and min(r_flag[i][1] for i in range(4)) == max(r_flag[i][1] for i in range(4)):
        print(r_flag[0][1],end='')
    else:
        print('(', end='')
        for i in range(4):
            if r_flag[i][0]: print(r_flag[i][1],end='')
            else:
                go(t//2,x,y) if i == 0 else go(t//2,x,y+t) if i == 1 else go(t//2,x+t,y) if i == 2 else go(t//2,x+t,y+t)
        print(')',end='')

n = int(input())
D = [input() for _ in range(n)]
if n==1:print(D[0])
go(n//2,0,0)