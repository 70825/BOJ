input=__import__('sys').stdin.readline
from collections import defaultdict
n = int(input())
D = [*map(int,input().split())]
k = defaultdict(lambda:0)
for i in range(n):
    k[D[i]]+=1
m = int(input())
D = [*map(int,input().split())]
ans = []
for i in range(m):
    ans.append(k[D[i]])
print(*ans)
