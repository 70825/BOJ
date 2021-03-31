l = int(input())
n = int(input())
roll_cake = [0]*(l+1)

maybe = [-1, -1] #예상길이, 방청객번호
real = [-1, -1] #실제길이, 방청객번호
for i in range(n):
    p, k = map(int,input().split())
    if k-p+1 > maybe[0]:
        maybe = [k-p+1,i+1]
    x = 0
    for j in range(p,k+1):
        if roll_cake[j] == 0:
            roll_cake[j] = 1
            x += 1
    if x > real[0]:
        real = [x, i+1]
print(maybe[1])
print(real[1])