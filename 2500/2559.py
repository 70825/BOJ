input = __import__('sys').stdin.readline
n, k = map(int,input().split())
D = [0]+[*map(int,input().split())]
for i in range(n):
    D[i+1] += D[i]
x, y = 0, k
ans = -float('inf')
while 1:
    if y > n: break
    ans = max(ans,D[y]-D[x])
    x+=1;y+=1
print(ans)