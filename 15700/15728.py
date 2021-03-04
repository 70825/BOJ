N,K=map(int,input().split())
A=input().split()
B=input().split()
for i in range(N):A[i]=int(A[i])
for i in range(N):B[i]=int(B[i])
B.sort()
for i in range(K):
    a=min(A)*min(B);b=min(A)*max(B);c=max(A)*min(B);d=max(A)*max(B)
    if a>=b and a>=c and a>=d:del B[0]
    elif b>=a and b>=c and b>=d:del B[len(B)-1]
    elif c>=a and c>=b and c>=d:del B[0]
    elif d>=a and d>=b and d>=c:del B[len(B)-1]
print(max(min(A)*min(B),max(A)*max(B),min(A)*max(B),max(A)*min(B)))