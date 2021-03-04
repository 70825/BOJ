N = int(input())
for i in range(N):
    A,B = map(int,input().split())
    print((min(A,B)-1)*2)