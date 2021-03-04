s=1
while 1:
    A=input();B=input()
    if A==B=='END':break
    a=[0]*26;b=[0]*26;k=0
    for i in range(len(A)):
        if 0<=ord(A[i])-97<=25:a[ord(A[i])-97]+=1
    for i in range(len(B)):
        if 0<=ord(B[i])-97<=25:b[ord(B[i])-97]+=1
    for i in range(26):
        if a[i]!=b[i]:k+=1
    print('Case '+str(s)+':',end=" ")
    if k==0:print('same')
    else:print('different')
    s+=1