n = int(input())
arr = sorted([*map(int,input().split())])

ans = 0
for i in range(n):
    ans += sum(arr[:i]) + arr[i]
print(ans)