N = int(input())
if 2<= N <=1000:
    cash = [None] * N
    for i in range(N):
        A = input()
        K = A.split(' ')
        if len(K) == 3:
            if 1<=int(K[0])<=6 and 1<=int(K[1])<=6 and 1<=int(K[2])<=6:
                if int(K[0]) == int(K[1]) == int(K[2]):
                    cash[i] = 10000 + (int(K[0]) * 1000)
                elif int(K[0]) == int(K[1]) or int(K[0]) == int(K[2]) or int(K[1]) == int(K[2]):
                    cash[i] = 1000 + max(int(K[0]),int(K[1]),int(K[2])) * 100
                else:
                    cash[i] = 100 * max(int(K[0]),int(K[1]),int(K[2]))
    print(max(cash))