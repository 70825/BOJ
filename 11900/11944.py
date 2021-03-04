N,M = map(str,input().split())
A = ""
B = ""
for i in range(int(N)):
    A += N
if len(A) <= int(M):
    print(A)
else:
    for i in range(int(M)//len(N)):
        B += N
    for i in range(int(M)%len(N)):
        B += N[i]
    print(B)