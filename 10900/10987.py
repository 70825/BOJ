T = str(input())
if 1<= len(T) <= 100 and T == T.lower():
    a=0
    for i in range(len(T)):
        if T[i] == "a" or T[i] == "e" or T[i] == "i" or T[i] == "o" or T[i] == "u":
            a += 1
    print(a)