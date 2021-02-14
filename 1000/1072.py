input=__import__('sys').stdin.readline
x, y = map(int,input().split())
win = (100*y)//x
l, r = 0, 10**9+1
while l <= r:
    mid = (l+r)//2
    z = int((y+mid)/(x+mid) * 100)
    if win < z:
        if win == int((100*(y+mid-1))//(x+mid-1)): print(mid);exit()
        r = mid - 1
    else: l = mid + 1
print(-1)