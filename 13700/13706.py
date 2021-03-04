n = int(input())
l,r = 0,n
while l <= r:
    mid = (l+r)//2
    if mid**2 == n:print(mid);exit()
    if mid**2 > n: r = mid - 1
    else: l = mid + 1