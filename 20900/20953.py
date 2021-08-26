input = __import__('sys').stdin.readline
for _ in range(int(input())):
    a, b = map(int, input().split())
    print((a + b) * (a + b - 1) * (a + b) // 2)