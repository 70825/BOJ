n = int(input())
k = int(input())
arr = sorted([*map(int, input().split())])
if k >= n:
    print(0)
    exit()
diff = sorted([arr[i+1]-arr[i] for i in range(n-1)])
print(sum(diff[:n-k]))