K = input()
A, B = K.split()
A = int(A)
B = int(B)
K = 1
if 1<=A<=1000 and 0<=B<=A:
    for i in range(A):
        K *= (i+1)
    for i in range(B):
        K //= (i+1)
    for i in range(A-B):
        K //= (i+1)
    print(K % 10007)