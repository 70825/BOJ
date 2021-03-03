a=["a"]*5
b=[]
for i in range(5):
    a[i] = str(input())
    for j in range(len(a[i])-2):
        if a[i][j]+a[i][j+1]+a[i][j+2] == "FBI":
            b.append(i+1)
B = list(set(b))
if len(B) == 0:
    print("HE GOT AWAY!")
else:
    for i in range(len(B)):
        print(B[i],end=" ")