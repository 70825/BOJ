input = __import__('sys').stdin.readline
n, q = map(int, input().split())
arr = [0]+[*map(int, input().split())]
psum = [0] * (n+1)
square = [0] * (n+1)
for i in range(1, n+1):
    psum[i] = psum[i-1] + arr[i]
    square[i] = square[i-1] + arr[i]**2
for i in range(q):
    a, b = map(int, input().split())
    print(((psum[b] - psum[a-1]) ** 2 - (square[b] - square[a-1])) // 2)