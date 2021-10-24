n = int(input())
if n == 0: print('NO'); exit()
count = 0
while n != 0:
    if n % 3 == 0: count = 0; n //= 3
    else:
        n -= 1
        count += 1
        if count > 1: print('NO'); exit()
print('YES')