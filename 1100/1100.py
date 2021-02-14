w=0
for i in range(8):
    A=str(input())
    if i%2==0:
        for j in range(8):
            if j%2==0 and A[j]=="F":
                w+=1
    else:
        for j in range(8):
            if j%2==1 and A[j]=="F":
                w+=1
print(w)