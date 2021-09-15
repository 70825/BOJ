n, W = map(int, input().split())
arr = [int(input()) for _ in range(n)]
stack = []
for i in range(n):
    if not stack: stack.append(arr[i])
    elif stack[-1] > arr[i]:
        min_val = float('inf')
        while stack:
            min_val = min(min_val, stack.pop())
        W = (W // min_val) * arr[i-1] + W % min_val
        stack.append(arr[i])
    else: stack.append(arr[i])
min_val = float('inf')
while stack:
    min_val = min(min_val, stack.pop())
W = (W // min_val) * arr[n-1] + W % min_val
print(W)