from collections import deque
def D(k):return (2*k)%10000,'D'
def S(k):
    if k==0:return 9999,'S'
    else:return k-1,'S'
def L(k):return (k%1000)*10+(k//1000),'L'
def R(k):return (k//10)+(k%10)*1000,'R'

for __ in range(int(input())):
    n,m=map(int,input().split())
    A,F,k=['']*10000,[-1]*10000,''
    q=deque([n])
    F[n]=-2
    while q:
        x=q.popleft()
        for i,j in [D(x),S(x),L(x),R(x)]:
            if F[i]==-1:
                q.append(i);A[i]=j;F[i]=x
    while m!=n:k+=A[m];m=F[m]
    print(k[::-1])