A = input()
N, M = A.split()
if len(N) <= 10 and len(M) <= 10:
    if int(N) == int(M):
        print("1")
    else:
        print("0")