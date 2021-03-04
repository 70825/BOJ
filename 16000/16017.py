A=[0,0,0,0];D=[8,9]
for i in range(4):A[i]=int(input())
if A[0] in D and A[3] in D:
    if A[1]==A[2]:print('ignore')
    else:print('answer')
else:print('answer')