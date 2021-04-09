def gcd(a,b):
    while b!=0:a,b=b,a%b
    return a
n = 1001
D = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if gcd(i,j) == 1:D[i][j] = 1
for i in range(n):
    for j in range(1,n):
        D[i][j] += D[i][j-1]
for j in range(n):
    for i in range(1,n):
        D[i][j] += D[i-1][j]
for _ in range(int(input())):
    x = int(input())
    print(D[x][x])