n = int(input())
D = sorted([*map(int,input().split())], key = lambda a:abs(a))
ans = [0,float('inf')]
for i in range(1,n):
    x = D[i-1]+D[i]
    if abs(x) < abs(sum(ans)):
        ans = [D[i-1],D[i]]
print(*sorted(ans))