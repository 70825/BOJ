import sys
while True:
    try:
        A,B = map(int,sys.stdin.readline().split())
        E = B-A+1
        for i in range(B-A+1):
            C = []
            D = str(i+A)
            for j in range(len(D)):
                C.insert(0,D[j])
            if len(C) != len(list(set(C))):
                E-=1
        print(E)
    except EOFError and ValueError:
        break