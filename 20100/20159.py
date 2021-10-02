input = __import__('sys').stdin.readline

n = int(input())
x = [0] + [*map(int, input().split())]
odd_psum = [0]
even_psum = [0]
for i in range(1, n+1):
    if i % 2:
        odd_psum.append(x[i] + odd_psum[-1])
        even_psum.append(even_psum[-1])
    else:
        odd_psum.append(odd_psum[-1])
        even_psum.append(x[i] + even_psum[-1])
ans = odd_psum[-1]
for i in range(1, n+1):
    if i % 2: val = odd_psum[i - 1] + (even_psum[-1] - even_psum[i])
    else: val = odd_psum[i] + (even_psum[-2] - even_psum[i-1])
    ans = max(ans, val)
print(ans)