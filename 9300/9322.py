for _ in range(int(input())):
    n = int(input())
    A1 = input().split()
    A2 = input().split()
    K = input().split()
    D = [A2.index(A1[i]) for i in range(n)]
    ans = [K[D[i]] for i in range(n)]
    print(' '.join(ans))