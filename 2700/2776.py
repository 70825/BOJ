from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    A = [*map(int,input().split())]
    Dict = defaultdict(lambda: 0)
    for i in range(n):
        Dict[A[i]] = 1
    m = int(input())
    B = [*map(int,input().split())]
    for i in range(m):
        print([0,1][Dict[B[i]]])