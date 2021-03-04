T=int(input())
for i in range(T):
    A=str(input());s=0
    for j in range(len(A)):
        if 65<=ord(A[j])<=90:s+=ord(A[j])-64
    if s==100:print('PERFECT LIFE')
    else:print(s)