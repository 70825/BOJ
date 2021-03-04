N,K,B = map(int,input().split())
A = input().split()
s = 0
for i in range(B-1,B+K-1,1):
    s += int(A[i%N])
print(s)