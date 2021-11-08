m, n = map(int, input().split())

count = 0
while m != 0:
    count += m
    m //= n
print(count)