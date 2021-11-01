input = __import__('sys').stdin.readline
for _ in range(int(input())):
    n, m = map(int, input().split())
    time = 0
    while n != 0:
        n //= 2
        time += 1
    if n != 1:print(time + m)
    else: print(time + m - 1)