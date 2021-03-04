input=__import__('sys').stdin.readline
n = int(input())
m = int(input())
light = [*map(int,input().split())]
ans = float('inf')
l,r = 0,n
while l <= r:
    mid = (l+r)//2
    length = [light[0]-mid,light[0]+mid]
    flag = True
    for x in light[1::]:
        if length[1] < x-mid: flag=False
        length[0] = min(length[0],x-mid)
        length[1] = max(length[1],x+mid)
    if not flag: l = mid + 1
    else:
        if length[0] <= 0 and length[1] >= n:
            ans = min(ans,mid)
            r = mid - 1
        else: l = mid + 1
print(ans)
