S = str(input())
d = 0
for i in range(len(S)):
    if S[i] == "A" or S[i] == "B" or S[i] =="C":
        d += 3
    elif S[i] == "D" or S[i] =="E" or S[i] =="F":
        d += 4
    elif S[i] == "G" or S[i] =="H" or S[i] =="I":
        d += 5
    elif S[i] == "J" or S[i] =="K" or S[i] =="L":
        d += 6
    elif S[i] == "M" or S[i] =="N" or S[i] =="O":
        d += 7
    elif S[i] == "P" or S[i] =="Q" or S[i] =="R" or S[i] =="S":
        d += 8
    elif S[i] == "T" or S[i] =="U" or S[i] =="V":
        d +=9
    elif S[i] == "W" or S[i] =="X" or S[i] =="Y" or S[i] =="Z":
        d += 10
print(d)