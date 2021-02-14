n = int(input())
D = [*map(int,input().split())]
ans = []
for i in range(n-1,-1,-1):
    ans = ans[:D[i]] + [i+1] + ans[D[i]:]
print(*ans)