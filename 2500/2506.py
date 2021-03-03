N = int(input())
A = input()
B = A.split()
s = 0
k = 0
for i in range(N):
    B[i] = int(B[i])
if B[0] == 1:
    k = 1
    s += k
for i in range(1,N,1):
    if B[i] == 0:
        k = 0
    elif B[i] == 1:
        if B[i-1] == 1:
            k+=1
            s += k
        else:
            k = 1
            s += k
print(s)