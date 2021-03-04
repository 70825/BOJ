T=int(input())
for i in range(T):
    A,B,C,D=map(int,input().split())
    if A+B*D==B*C:print('does not matter')
    elif A+B*D<B*C:print('parallelize')
    else:print('do not parallelize')