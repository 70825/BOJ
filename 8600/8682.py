input = __import__('sys').stdin.readline
for _ in range(int(input())):
    n, d = map(int,input().split())
    if d > n: d %= n
    a, b = n, d
    while b != 0: a,b = b,a%b
    print(n//a)