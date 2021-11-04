input = __import__('sys').stdin.readline

n, t = map(int, input().split())
psum = [0] * (100002)
for i in range(n):
    k = int(input())
    for j in range(k):
        s, e = map(int, input().split())
        psum[s] += 1
        psum[e] -= 1
arr = [0] * (100002)
arr[0] = psum[0]
for i in range(1, 100002):
    arr[i] = arr[i-1] + psum[i]
s, e = 0, t
val = 0
for i in range(t):
    val += arr[i]
ans = [val, s, e]
for i in range(t, 100002):
    val -= arr[s]
    s += 1
    val += arr[e]
    e += 1
    if val > ans[0]: ans = [val, s, e]
print(ans[1], ans[2])