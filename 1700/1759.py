def go(n,alpha,password,i):
    if len(password)==n:
        if check(password):
            print(password)
        return
    if i>=len(alpha):return
    go(n,alpha,password+alpha[i],i+1)
    go(n,alpha,password,i+1)

def check(A):
    a=0;b=0
    for i in range(len(A)):
        if A[i] in 'aeiou':a+=1
        else:b+=1
    return a>=1 and b>=2

L,C=map(int,input().split())
D=sorted([*map(str,input().split())])
go(L,D,'',0)