import sys
N = int(input())
d = 1
for i in range(N):
    d += int(sys.stdin.readline()) -1
print(d)