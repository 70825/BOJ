T = int(input())
for i in range(T):
    K = input()
    K_list = K.split(' ')
    H = int(K_list[0])
    W = int(K_list[1])
    N = int(K_list[2])
    Y, X = divmod(N-1, H)
    print((X+1) * 100  + (Y+1))