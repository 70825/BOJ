for i in range(int(input())):
    A,B=map(int,input().split())
    if A**(1/3)==int(A**(1/3)):k=int(A**(1/3))
    else:k=int(A**(1/3))+1
    p=int(B**(1/3))+1
    ans=0
    for j in range(k,p):
        ans+=1
    print('Case #'+str(i+1)+':',end=" ")
    print(ans)