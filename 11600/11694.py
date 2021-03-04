n = int(input())
D = [*map(int,input().split())]
ans = 0
one = 0
for i in range(n):
    if D[i]==1:one+=1
    ans ^= D[i]
if one == n:print(['koosaga','cubelover'][one%2])
else:
    if ans:print('koosaga')
    else:print('cubelover')
