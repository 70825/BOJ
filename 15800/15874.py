A,B=map(int,input().split())
C=str(input())
for i in range(len(C)):
    k=A%26
    if 0<=ord(C[i])-65<=25:
        if ord(C[i])-65+k>25:print(chr(ord(C[i])-26+k),end="")
        else:print(chr(ord(C[i])+k),end="")
    elif 0<=ord(C[i])-97<=25:
        if ord(C[i])-97+k>25:print(chr(ord(C[i])-26+k),end="")
        else:print(chr(ord(C[i])+k),end="")
    else:print(C[i],end="")