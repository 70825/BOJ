N = int(input())
if 1<= N < 1000:
    J = 1000 - N
    c = 0
    while 1:
        if J >= 500:
            J -= 500
            c += 1
        elif J >= 100:
            J -= 100
            c += 1
        elif J >= 50:
            J -= 50
            c += 1
        elif J >= 10:
            J -= 10
            c += 1
        elif J >= 5:
            J -= 5
            c += 1
        elif J >= 1:
            J -= 1
            c += 1
        else:
            break
    print(c)