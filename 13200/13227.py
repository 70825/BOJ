A=[[]*3 for i in range(3)]
for i in range(3):
    A[i]=str(input())
B='XXX';C='OOO'
if A[0]==B or A[1]==B or A[2]==B or A[0]==C or A[1]==C or A[2]==C:
    print('YES')
elif A[0][0]+A[1][1]+A[2][2]==C or  A[0][0]+A[1][1]+A[2][2]==B:
    print('YES')
elif A[2][0]+A[1][1]+A[0][2]==B or A[2][0]+A[1][1]+A[0][2]==C:
    print('YES')
elif A[0][0]+A[1][0]+A[2][0]==B or A[0][0]+A[1][0]+A[2][0]==C:
    print('YES')
elif A[0][1]+A[1][1]+A[2][1]==B or A[0][1]+A[1][1]+A[2][1]==C:
    print('YES')
elif A[0][2]+A[1][2]+A[2][2]==B or A[0][2]+A[1][2]+A[2][2]==C:
    print('YES')
else:print('NO')