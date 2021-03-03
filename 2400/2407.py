n,m = input().split()
n = int(n)
m = int(m)
a = 1
if 5<=n<=100 and 5<=m<=100 and m<=n:
    for i in range(n):
        a *= (i+1)
    for i in range(m):
        a //= (i+1)
    for i in range(n-m):
        a //= (i+1)
    print(a)