for i in range(int(input())):
    A=input().split()
    print('Case '+str(i+1)+':',end=" ")
    for j in range(len(A)):
        if A[j]=='.-':print('A',end="")
        elif A[j]=='-...':print('B',end="")
        elif A[j]=='-.-.':print('C',end="")
        elif A[j]=='-..':print('D',end="")
        elif A[j]=='.':print('E',end="")
        elif A[j]=='..-.':print('F',end="")
        elif A[j]=='--.':print('G',end="")
        elif A[j]=='....':print('H',end="")
        elif A[j]=='..':print('I',end="")
        elif A[j]=='.---':print('J',end="")
        elif A[j]=='-.-':print('K',end="")
        elif A[j]=='.-..':print('L',end="")
        elif A[j]=='--':print('M',end="")
        elif A[j]=='-.':print('N',end="")
        elif A[j]=='---':print('O',end="")
        elif A[j]=='.--.':print('P',end="")
        elif A[j]=='--.-':print('Q',end="")
        elif A[j]=='.-.':print('R',end="")
        elif A[j]=='...':print('S',end="")
        elif A[j]=='-':print('T',end="")
        elif A[j]=='..-':print('U',end="")
        elif A[j]=='...-':print('V',end="")
        elif A[j]=='.--':print('W',end="")
        elif A[j]=='-..-':print('X',end="")
        elif A[j]=='-.--':print('Y',end="")
        elif A[j]=='--..':print('Z',end="")
    print("")