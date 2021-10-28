input = __import__('sys').stdin.readline
from collections import defaultdict

n, p = map(int, input().split())
w, l, g = map(int, input().split())
text = defaultdict(lambda : "U")
for i in range(p):
    a, b = input().strip().split()
    text[a] = b
arr = [input().strip() for _ in range(n)]
score = 0
for i in range(n):
    if text[arr[i]] == "W":
        score += w
        if score >= g: print("I AM NOT IRONMAN!!"); exit()
    else: score = max(0, score - l)
print("I AM IRONMAN!!")