T=int(input())
A=[];a=0;b=0
N=input().split()
M=input().split()
for i in range(T):
    a+=int(N[i])
    b+=int(M[i])
    if a==b:A.append(i+1)
if len(A)==0:print(0)
else:print(max(A))