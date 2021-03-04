import sys
a = [0] * 5
total = 0
for i in range(5):
    a[i] = int(input())
    if 0 <= a[i] <= 100 and a[i] % 5 == 0:
        if a[i] < 40:
            a[i] = 40
        total += a[i]
    else:
        sys.exit(1)
print(int(total / 5))