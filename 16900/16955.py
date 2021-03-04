K=['.XXXX','X.XXX','XX.XX','XXX.X','XXXX.']
D=[[*input()] for _ in range(10)]
k=0
def A(a,b):
    return D[a][b]+D[a][b+1]+D[a][b+2]+D[a][b+3]+D[a][b+4]
def B(a,b):
    return D[a][b]+D[a+1][b+1]+D[a+2][b+2]+D[a+3][b+3]+D[a+4][b+4]
def C(a,b):
    return D[a][b]+D[a+1][b-1]+D[a+2][b-2]+D[a+3][b-3]+D[a+4][b-4]
def E(a,b):
    return D[a][b]+D[a+1][b]+D[a+2][b]+D[a+3][b]+D[a+4][b]
for i in range(10):
    for j in range(6):
        if A(i,j) in K:k=1
for i in range(6):
    for j in range(10):
        if E(i,j) in K:k=1
for i in range(6):
    for j in range(6):
        if B(i,j) in K:k=1
for i in range(6):
    for j in range(4,10):
        if C(i,j) in K:k=1
print(k)