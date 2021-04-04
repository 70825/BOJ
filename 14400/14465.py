input = __import__('sys').stdin.readline
n,k,b = map(int,input().split())
D = [0]*(n+1)
for i in range(b):
    D[int(input())] = 1
for i in range(n):
    D[i+1] += D[i]
ans = float('inf')
x,y = 0,k
while y <= n:
    ans = min(ans, D[y]-D[x])
    x+=1;y+=1
print(ans)