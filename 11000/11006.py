t = int(input())
while t:
    N, M = map(int,input().split())
    U = 2 * M - N
    T = M - U
    print(U, T)
    t -= 1