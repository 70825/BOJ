T=int(input())
print(T,end=" ")
while T!=1:
    if T % 2==0:T=T//2;print(T,end=" ")
    else:T=3*T+1;print(T,end=" ")