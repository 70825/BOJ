N = int(input())
A = [0] * N
for i in range(N):
    D = input()
    B = D.split()
    C = []
    for j in range(5):
        B[j] = int(B[j])
        C.insert(j,B[j])
    C.remove(max(C))
    C.remove(min(C))
    if max(C)-min(C) >= 4:
        print("KIN")
    else:
        print(sum(B)-max(B)-min(B))