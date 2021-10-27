n, m, l = map(int, input().split())
arr = [0, l] if not n else [0] + sorted([*map(int, input().split())]) + [l]
diff = [arr[i+1] - arr[i] for i in range(len(arr)-1)]
for x in range(1, l):
    val = 0
    for i in range(len(diff)):
        val += diff[i] // x
        if diff[i] % x == 0: val -= 1
    if val <= m: print(x);break