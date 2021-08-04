def check():
    flag = True
    for i in range(n):
        for j in range(m):
            if s[i][j] != answer[i][j]:
                flag = False
    return flag

n, m = map(int, input().split())
s = [[*input()] for _ in range(n)]
answer = [[*input()] for _ in range(n)]
if n < 3 and m < 3:
    print([-1, 0][check()])
    exit()

ans = 0
for i in range(n - 2):
    for j in range(m - 2):
        if s[i][j] != answer[i][j]:
            ans += 1
            for x in range(i, i+3):
                for y in range(j, j+3):
                    s[x][y] = '1' if s[x][y] == '0' else '0'

print([-1, ans][check()])