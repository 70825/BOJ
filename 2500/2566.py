A = [[0] * 9 for i in range(9)]
m = 0
a = 0
b = 0
for i in range(9):
    A[i][0],A[i][1],A[i][2],A[i][3],A[i][4],A[i][5],A[i][6],A[i][7],A[i][8]= map(int,input().split())

for i in range(9):
    for j in range(9):
        if A[i][j] > m:
            m = A[i][j]
            a = i
            b = j
print(m)
print(a+1,b+1)