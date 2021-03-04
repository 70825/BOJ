a = str(input())
T = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for i in range(len(a)):
    if a[i] == "A":
        print("X", end="")
    elif a[i] == "B":
        print("Y", end="")
    elif a[i] == "C":
        print("Z", end="")
    else:
        for j in range(26):
            if a[i] == T[j]:
                print(chr(65+j-3),end="")
print("")