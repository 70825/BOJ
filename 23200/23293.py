from collections import defaultdict
input = __import__('sys').stdin.readline

t, n = map(int, input().split())
now = [1] * (n+1)
item = [defaultdict(lambda: 0) for _ in range(n)]
log = []
ans = set()
for i in range(t):
    num, player, val, *arr = input().strip().split()
    num = int(num); player = int(player)

    if val == "M": now[player-1] = int(arr[0])
    elif val == "F":
        if now[player-1] != int(arr[0]): log.append(num)
        item[player-1][int(arr[0])] += 1
    elif val == "C":
        if item[player-1][int(arr[0])] == 0 or item[player-1][int(arr[1])] == 0:
            log.append(num)
            item[player - 1][int(arr[0])] = max(item[player - 1][int(arr[0])] - 1, 0)
            item[player - 1][int(arr[1])] = max(item[player - 1][int(arr[1])] - 1, 0)
        else:
            item[player - 1][int(arr[0])] -= 1
            item[player - 1][int(arr[1])] -= 1
    else:
        if now[player-1] != now[int(arr[0])-1]:
            log.append(num)
            ans.add(player)
print(len(log))
if len(log): print(*log)
ans = sorted([*ans])
print(len(ans))
if len(ans): print(*ans)