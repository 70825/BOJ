K = input()
M = K.split(' ')
P = [1,1,2,2,2,8]
for i in range(len(M)):
    if 0<=int(M[i])<=10:
        print(P[i]-int(M[i]),end=" ")