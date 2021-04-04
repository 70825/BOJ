input = __import__('sys').stdin.readline
n, k = map(int,input().split())
max_n = 10**6+1
D = [0]*max_n
for i in range(n):
    g,x = map(int,input().split())
    D[x] = g
for i in range(1,max_n):
    D[i] += D[i-1]
ans = 0
if 2*k+1 >= max_n: ans = D[max_n-1]
else:
    for y in range(2*k+1, max_n):
        x = y - 2*k
        ans = max(ans, D[y]-D[x-1])
print(ans)