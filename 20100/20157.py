from math import gcd
from collections import defaultdict as dfd
input = __import__('sys').stdin.readline
one = dfd(lambda : 0)
two = dfd(lambda : 0)
three = dfd(lambda : 0)
four = dfd(lambda : 0)
plus_x, minus_x, plus_y, minus_y = 0, 0, 0, 0
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    if x == 0:
        if y > 0: plus_y += 1
        else: minus_y += 1
        continue
    if y == 0:
        if x > 0: plus_x += 1
        else: minus_x += 1
        continue
    vx, vy = abs(x), abs(y)
    g = gcd(vx, vy)
    nx, ny = vx // g,  vy // g
    if x > 0 and y > 0: one[str(nx)+'/'+str(ny)] += 1
    if x < 0 and y > 0: two[str(nx)+'/'+str(ny)] += 1
    if x < 0 and y < 0: three[str(nx)+'/'+str(ny)] += 1
    if x > 0 and y < 0: four[str(nx)+'/'+str(ny)] += 1
ans = 0
if len(one.values()) > 0: ans = max(ans, max(one.values()))
if len(two.values()) > 0: ans = max(ans, max(two.values()))
if len(three.values()) > 0: ans = max(ans, max(three.values()))
if len(four.values()) > 0: ans = max(ans, max(four.values()))
print(max(ans, plus_x, minus_x, plus_y, minus_y))