N = int(input())
n = 1
while N > 1:
    if N % 2 == 1:
        n+=1
        N = 3*N+1
    else:
        n+=1
        N /= 2
print(n)