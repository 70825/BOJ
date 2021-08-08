n, m = map(int, input().split())
arr = sorted([*map(int, input().split())])
plus = []
minus = []
for i in range(n):
    if arr[i] > 0: plus.append(arr[i])
    else: minus.append(arr[i])

plus_val = [plus[i] for i in range(len(plus) - 1, -1, -m)]
minus_val = [abs(minus[i]) for i in range(0, len(minus), m)]

plus_sum = sum(plus_val)
minus_sum = sum(minus_val)

if len(plus_val) == 0: print(minus_sum * 2 - minus_val[0])
elif len(minus_val) == 0: print(plus_sum * 2 - plus_val[0])
elif plus[-1] > abs(minus[0]): print(2 * (plus_sum + minus_sum) - plus_val[0])
else: print(2 * (plus_sum + minus_sum) - minus_val[0])