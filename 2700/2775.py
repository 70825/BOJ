T = int(input())
for z in range(T):
    k = int(input())  # k층
    n = int(input())  # n호
    if 1<= k <= 14 and 1<= n <= 14:
        P = [[0] * n for i in range(k+1)]
        for j in range(n):
            P[0][j] = j+1
        for i in range(1,k+1):
            for j in range(n):
                q = 0
                for u in range(j+1):
                    q += P[i-1][u]
                P[i][j] = q
        print(P[k][n-1])