n = int(input())
arr = sorted([int(input()) for i in range(n)], reverse=True)
print(sum(arr[i] for i in range(n) if i % 3 < 2))