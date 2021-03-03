M = int(input())
A = [0] * 3
for i in range(3):
    A[i] = i+1
if 1<=M<=50:
    for i in range(M):
        B = input()
        X,Y = B.split(' ')
        X = int(X)
        Y = int(Y)
        if 0< X <=3 and 0<Y<=3:
            temp = A[X-1]
            A[X-1] = A[Y-1]
            A[Y-1] = temp
        else:
            break
    for i in range(3):
        if A[i] == 1:
            print(i+1)
        elif min(A) != 1:
            print("-1")