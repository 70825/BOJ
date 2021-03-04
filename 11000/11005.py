N,B=map(int,input().split())
S=[]
while N!=0:
    if N%B<=9:
        S.append(N%B)
    else:
        S.append(chr(N%B+55))
    N//=B
print(''.join(map(str,S[::-1])))