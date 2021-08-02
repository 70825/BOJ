input = __import__('sys').stdin.readline
n = int(input())
arr = sorted(int(input()) for i in range(n))
ans = 0
for i in range(n):
    ans += abs(arr[i] - (i+1))
print(ans)
