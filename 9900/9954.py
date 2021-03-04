while 1:
    A=input()
    if A=='#':break
    sub_memo=A[len(A)-1]
    memo=ord(sub_memo)-ord('A')
    for i in range(len(A)-1):
        if 65<=ord(A[i])<=90:
            if ord(A[i])-memo<65:print(chr(ord(A[i])-memo+26),end="")
            else:print(chr(ord(A[i])-memo),end="")
        elif 97<=ord(A[i])<=122:
            if ord(A[i])-memo<97:print(chr(ord(A[i])-memo+26),end="")
            else:print(chr(ord(A[i])-memo),end="")
        else:print(A[i],end="")
    print("")