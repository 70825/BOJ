A = int(input())
for i in range(A):
    a = 0
    N = str(input())
    M = str(input())
    if len(N) <= 100 and len(N) == len(M):
        for j in range(len(N)):
            if N[j] != M[j]:
                a+=1
        print("Hamming distance is "+str(a)+".")