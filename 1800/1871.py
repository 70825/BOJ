for i in range(int(input())):
    A=input().split('-');B=0
    for j in range(len(A[0])):
        B+=(ord(A[0][len(A[0])-1-j])-65)*26**j
    if abs(B-int(A[1]))<=100:print('nice')
    else:print('not nice')