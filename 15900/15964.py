K = input()
A, B = K.split()
A = int(A)
B = int(B)
if 1<=A<=100000 and 1<=B<=100000:
    print((A+B)*(A-B))