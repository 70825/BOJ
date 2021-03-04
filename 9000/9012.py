T = int(input())
for i in range(T):
    s = 0
    d = 0
    A = str(input())
    for j in range(len(A)):
        if A[j] == "(":
            s += 1
        else:
            d += 1
            if d > s:
                d = 0
                break
    if s + d == len(A) and s == d:
        print("YES")
    else:
        print("NO")