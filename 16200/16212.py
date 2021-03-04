n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
a.sort()
for i in range(n):
    print(a[i],end=" ")