D=['a','e','i','o','u','A','E','I','O','U']
for i in range(int(input())):
    A=input()
    print('Case #'+str(i+1)+':',end=" ")
    if A[len(A)-1]=='y' or A[len(A)-1]== 'Y':
        print(A,'is ruled by nobody.')
    elif A[len(A)-1] in D:
        print(A,'is ruled by a queen.')
    else:
        print(A, 'is ruled by a king.')