N = int(input())
A = [0]*5
A[0],A[1],A[2],A[3],A[4] = map(int,input().split())
c = 0
for i in range(5):
    if A[i] == N:
        c += 1
print(c)