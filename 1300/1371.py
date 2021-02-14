d=[0]*26
while 1:
    try:
        A=str(input())
        for i in range(len(A)):
            if 97<=ord(A[i])<=122:
                for j in range(26):
                    if A[i] == chr(j+97):
                        d[j]+=1
    except EOFError:
        for i in range(26):
            if d[i] == max(d):
                print(chr(i+97),end="")
        break