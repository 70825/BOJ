input = __import__('sys').stdin.readline
from collections import defaultdict as dd

n = int(input())
D = [int(input()) for i in range(n)]
#산술평균
z = sum(D)
x = abs(z)
y = x%n
if n%2 == 0 and y >= n//2:
    if z>=0:print(x//n+1)
    else:print(-(x//n)-1)
elif n%2 == 0:
    if z>=0:print(x//n)
    else:print(-(x//n))
elif n%2 and y > n//2:
    if z>=0: print(x//n+1)
    else:print(-(x//n)-1)
else:
    if z>=0:print(x//n)
    else:print(-(x//n))
#중앙값
S = sorted(D)
print(S[n//2])
#최빈값
k = dd(lambda: 0)
for i in range(n):
    k[S[i]]+=1
ans = [-1,[]]
for x in k.keys():
    if k[x] > ans[0]:
        ans = [k[x],[x]]
    elif k[x] == ans[0]:
        ans[1].append(x)
if len(ans[1]) >= 2:print(sorted(ans[1])[1])
else:print(*ans[1])
#범위
print(max(D)-min(D))