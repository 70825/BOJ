import sys
N,K = map(int,input().split())
B = sys.stdin.readline().split()
for i in range(N):
    B[i] = int(B[i])
B.sort()
print(B[K-1])