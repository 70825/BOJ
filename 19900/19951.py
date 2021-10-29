input = __import__('sys').stdin.readline
n, m = map(int, input().split())
h = [0] + [*map(int, input().split())]
temp = [0] * (n+2)
psum = [0] * (n+2)
for i in range(m):
    a, b, k = map(int, input().split())
    temp[a] += k
    temp[b+1] -= k
for i in range(1, n+1):
    psum[i] = psum[i-1] + temp[i]
for i in range(1, n+1):
    h[i] += psum[i]
print(*h[1:])