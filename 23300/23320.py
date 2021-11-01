n = int(input())
a = [*map(int, input().split())]
x, y = map(int, input().split())
p = x * len(a) // 100
q = sum(1 for i in range(len(a)) if a[i] >= y)
print(p, q)