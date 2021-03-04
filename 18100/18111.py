input = __import__('sys').stdin.readline
n,m,b = map(int,input().split())
D = [[*map(int,input().split())] for _ in range(n)]
min_val = min(D[i][j] for i in range(n) for j in range(m))
max_val = max(D[i][j] for i in range(n) for j in range(m))
S = [0]*(max_val+1)
for i in range(n):
    for j in range(m):
        S[D[i][j]]+=1
ans = [float('inf'),0]
for x in range(min_val,max_val+1):
    time, z = 0,b
    for i in range(min_val,x):
        time += S[i]*(x-i)
        z -= S[i]*(x-i)
    for i in range(x+1,max_val+1):
        time += 2*S[i]*(i-x)
        z += S[i]*(i-x)
    if ans[0] > time and z >= 0:ans = [time,x]
    if ans[0] == time and z >= 0:ans[1] = x
print(*ans)