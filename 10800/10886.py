N = int(input())
cute = 0
if 1<= N <= 101 and N % 2 == 1:
    C = 0
    for i in range(N):
        C = int(input())
        if C == 1:
            cute += 1
        elif C == 0:
            cute -= 1
        else:
            cute = 0
            break
    if cute > 0:
        print("Junhee is cute!")
    elif cute < 0:
        print("Junhee is not cute!")