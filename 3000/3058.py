N = int(input())
for i in range(N):
    even = 0
    B = [0] * 7
    C = [101] * 7
    K = input()
    A = K.split()
    
    for j in range(7):
        if int(A[j]) % 2 == 0:
            even +=1
            B[j] = int(A[j])
            C[j] = int(A[j])
    if int(min(A))>=1 and int(max(A)) <= 100 and even >= 1:
        print(sum(B), min(C))