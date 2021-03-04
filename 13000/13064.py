for i in range(int(input())):
    S=str(input())
    if S[0]==S[1] and 49<=ord(S[0])<=57 and 49<=ord(S[2])<=57 and 49<=ord(S[3])<=57 and 65<=ord(S[4])<=90 and 49<=ord(S[5])<=57 and 49<=ord(S[6])<=57 and 49<=ord(S[7])<=57:
        print(S)