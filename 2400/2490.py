for i in range(3):
    N = str(input())
    K = N.split(' ')
    count = 0
    for j in range(len(K)):
        if int(K[j]) == 0:
            count += 1
    if count == 0:
        print("E")
    elif count == 1:
        print("A")
    elif count == 2:
        print("B")
    elif count == 3:
        print("C")
    elif count == 4:
        print("D")