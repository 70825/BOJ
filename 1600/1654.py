k, n = map(int,input().split())
line = [int(input()) for i in range(k)]
l, r = 1,max(line)
ans = 0
while l <= r:
    mid = (l+r)//2
    val = 0
    for x in line:
        val += x//mid
    if val >= n:
        ans = max(ans,mid)
        l = mid + 1
    else:r = mid - 1
print(ans)