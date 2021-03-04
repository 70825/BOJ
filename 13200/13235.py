A=str(input());A=A.lower();b=len(A)//2;d=0
if len(A)%2==0:
    for j in range(b):
        if A[b-1-j]==A[b+j]:d+=1
    if d==b:print('true')
    else:print('false')
else:
    for j in range(b):
        if A[b-j-1]==A[b+j+1]:d+=1
    if d==b:print('true')
    else:print('false')