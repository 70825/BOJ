input=__import__('sys').stdin.readline
D=[2,22,222,3,33,333,4,44,444,5,55,555,6,66,666,7,77,777,7777,8,88,888,9,99,999,9999]
for i in range(int(input())):
    A=str(input()).lower()
    k=''
    print('Case #'+str(i+1)+':',end=" ")
    if len(k)==0:
        if A[0]==' ':k+='0'
        else:k+=str(D[ord(A[0])-97])
    for j in range(1,len(A)-1):
        if A[j]==' ':s='0'
        else:s=str(D[ord(A[j])-97])
        if k[len(k)-1]==s[0]:k+=' '+s
        else:k+=s
    print(k)