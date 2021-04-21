r, c = map(int,input().split())
arr = list(list(map(int,input().split())) for _ in range(r))
t = int(input())

ans = 0
for i in range(r-2):
    for j in range(c-2):
        D = []
        for x in range(3):
            for y in range(3):
                D.append(arr[i+x][j+y])
        if sorted(D)[4] >= t: ans += 1
print(ans)