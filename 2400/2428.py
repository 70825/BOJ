input=__import__('sys').stdin.readline
n = int(input())
F = sorted([*map(int,input().split())])
ans = 0
for i in range(1,n):
    l,r = 0,i
    while l <= r:
        mid = (l+r)//2
        if F[i]*9 <= F[mid]*10:
            if F[i]*9 > F[mid-1]*10:break
            r = mid - 1
        else: l = mid + 1
    ans += i - mid
print(ans)