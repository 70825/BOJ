A = input()
R1,S=A.split()
if -1000<=int(R1)<=1000 and -1000<=int(S)<=1000:
    R2 = 2*int(S) - int(R1)
    print(R2)