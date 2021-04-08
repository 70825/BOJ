n = int(input())
D = [*map(int,input().split())]
if n == 1: print(str(D[0])+'/1');exit()
x = 1
for i in range(n):
    x *= D[i]
y = 0
for i in range(n):
    y += x // D[i]
a, b = x, y
while b!=0:a,b=b,a%b

if x >= y and x % y == 0: print(x//y)
else: print(str(x//a)+'/'+str(y//a))