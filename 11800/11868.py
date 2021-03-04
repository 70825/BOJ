n = int(input())
D = [*map(int,input().split())]
ans = 0
for i in range(n):ans ^= D[i]
if ans:print('koosaga')
else:print('cubelover')