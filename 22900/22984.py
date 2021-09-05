n = int(input())
p = [*map(float, input().split())]
print(sum(p) + sum([p[i] * (1 - p[i-1]) + (1 - p[i]) * p[i-1] for i in range(1, n)]))