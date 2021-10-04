n = int(input())
arr = []
val = 0
num = 1
while val < n:
    val += len(str(num))
    num += 1
print(str(num-1)[min(val, n) - max(val, n) - 1])