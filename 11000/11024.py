T = int(input())
for i in range(T):
    a = input().split()
    for j in range(len(a)):
        a[j] = int(a[j])
    print(sum(a))