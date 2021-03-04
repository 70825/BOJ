input=__import__('sys').stdin.readline
n,m = map(int,input().split())
A = sorted([int(input()) for i in range(n)])
for i in range(m):
    x = int(input())
    l,r = 0, n-1
    while l <= r:
        mid = (l+r)//2
        if A[mid] >= x:
            if mid != 0 and A[mid-1] < x:break
            r = mid - 1
        else: l = mid + 1
    print(mid) if A[mid] == x else print(-1)
