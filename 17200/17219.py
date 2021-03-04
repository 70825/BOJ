n,m = map(int,input().split())
d = {}
for i in range(n):
    a,b = input().split()
    d[a] = b
for i in range(m):
    print(d[input()])