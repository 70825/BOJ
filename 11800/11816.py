N=str(input())
k=10
if N[0]=='0':
    if N[1]=='x':k=16
    else:k=8
print(int(N,k))