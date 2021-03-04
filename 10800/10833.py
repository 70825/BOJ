T = int(input())
A = [0] * T
for i in range(T):
    B,C = map(int,input().split())
    A[i] = C % B
print(sum(A))