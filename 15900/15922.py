n = int(input())
arr = [[*map(int, input().split())] for _ in range(n)]
s, e = arr[0]
ans = abs(e - s)
for i in range(1, n):
    ns, ne = arr[i]
    if ns <= e and ne > e:
        ans += abs(ne - e)
        e = ne
    elif ns > e:
        ans += abs(ne - ns)
        s, e = ns, ne
print(ans)