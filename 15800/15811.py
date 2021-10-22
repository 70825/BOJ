input = __import__('sys').stdin.readline
a, b, c = map(list, input().strip().split())
arr = [*set(a+b+c)]
val = {}
num = [i for i in range(10)]
if len(arr) > 10: print('NO');exit()
for choose in __import__('itertools').permutations(num, len(arr)):
    for i in range(len(arr)):
        val[arr[i]] = choose[i]
    x = y = z = 0
    for k in [*a]: x = x * 10 + val[k]
    for k in [*b]: y = y * 10 + val[k]
    for k in [*c]: z = z * 10 + val[k]
    if x + y == z:print('YES');exit()
print('NO')