n, k = map(int, input().split())
arr = sorted([*map(int, input().split())])
diff = sorted([arr[i+1] - arr[i] for i in range(n-1)])
print(sum(diff[:n-k]))