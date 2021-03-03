n = int(input())
D = sorted([*map(int,input().split())])
x,y = 0,n-1
ans = float('inf')
val = [0,0]
while x!=y:
    if ans > abs(D[x]+D[y]):
        ans = abs(D[x]+D[y])
        val = [D[x],D[y]]
    if abs(D[x]) <= abs(D[y]):y-=1
    else:x+=1
print(*val)