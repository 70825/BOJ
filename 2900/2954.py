A=str(input());S=0
while S!=len(A):
    if A[S]=='e' or A[S]=='a' or A[S]=='i' or A[S]=='o' or A[S]=='u':
        print(A[S],end="");S+=3
    else:print(A[S],end="");S+=1
    if S>len(A):break