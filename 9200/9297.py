T=int(input())
for i in range(T):
    A,B=map(int,input().split())
    if A//B!=0 and A%B!=0:print('Case '+str(i+1)+':',A//B,str(A%B)+'/'+str(B))
    elif A//B==0 and A%B!=0:print('Case '+str(i+1)+':',str(A%B)+'/'+str(B))
    elif A//B!=0 and A%B==0:print('Case '+str(i+1)+':',A//B)
    else:print('Case '+str(i+1)+':',0)