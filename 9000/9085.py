T = int(input())
for i in range(T):
    N = int(input())
    a = input().split()
    for j in range(N):
        a[j] = int(a[j])
    print(sum(a))