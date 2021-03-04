A = input().split('|')
a = 0
c = 0
d = 0
e = A[len(A)-1][len(A[len(A)-1])-1]
for i in range(len(A)):
    if A[i][0] == "A" or A[i][0] == "E" or A[i][0] == "D":
        a += 1
    elif A[i][0] == "C" or A[i][0] == "F" or A[i][0] == "G":
        c += 1
if a>c:
    print("A-minor")
elif c>a:
    print("C-major")
elif c==a:
    if e == "A" or e == "E" or e == "D":
        print("A-minor")
    elif e == "C" or e == "F" or e == "G":
        print("C-major")