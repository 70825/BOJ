input=__import__('sys').stdin.readline

for _ in range(int(input())):
    l, n = map(int,input().split())
    pos = [int(input()) for i in range(n)]
    fast = max(min(l-pos[i],pos[i]) for i in range(n))
    slow = max(max(l-pos[i],pos[i]) for i in range(n))
    print(fast,slow)