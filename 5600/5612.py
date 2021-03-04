T = int(input())
d = int(input())
a = [0] * T
a[0] += d
for i in range(T):
    b,c = map(int,input().split())
    if i == 0:
        a[i] += b-c
    else:
        a[i] += a[i-1] +b-c
if min(a) < 0:
    print("0")
else:
    print(max(a))