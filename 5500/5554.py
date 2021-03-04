a = 0
for i in range(4):
    b = int(input())
    a += b
if 60 <= a <=59*60+59:
    print(a // 60)
    print(a % 60)