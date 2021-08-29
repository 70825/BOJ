input = __import__('sys').stdin.readline
n, m = map(int, input().split())
a = [*map(int, input().split())]
dfd = __import__('collections').defaultdict(lambda: __import__('collections').deque())
for i in range(n):
    dfd[a[i]].append(i+1)
reverse = 0
val = 0
for x in sorted(dfd.keys())[::-1]:
    while dfd[x]:
        if not reverse: print(dfd[x].popleft())
        else:print(dfd[x].pop())
        if x % 7 == 0: reverse ^= 1
        val += 1
        if val == m: exit()