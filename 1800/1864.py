A=['-','\\','(','@','?','>','&','%','/']
while 1:
    B = str(input())
    if B=='#':
        break
    else:
        C = 0
        for i in range(len(B)):
            for j in range(9):
                if B[i] == '/' and j == 8:
                    C += (-1) * 8 ** (len(B) - 1 - i)
                else:
                    if B[i] == A[j]:
                        C += j * 8 ** (len(B) - 1 - i)
        print(C)