A=str(input())
B=str(input())
for i in range(len(A)):
    if A[i]==B[i]=='1':print(1,end="")
    else:print(0,end="")
print("")
for i in range(len(A)):
    if A[i]=='1' or B[i]=='1':print(1,end="")
    else:print(0,end="")
print("")
for i in range(len(A)):
    if A[i]=='1'==B[i]:print(0,end="")
    elif A[i]=='1' or B[i]=='1':print(1,end="")
    else:print(0,end="")
print("")
for i in range(len(A)):
    if A[i]=='1':print(0,end="")
    else:print(1,end="")
print("")
for i in range(len(A)):
    if B[i]=='1':print(0,end="")
    else:print(1,end="")
print("")