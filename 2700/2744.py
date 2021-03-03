N = (input())
if len(N) <= 100:
    for i in range(len(N)):
        a = N[i]
        if N[i] == N[i].upper():
            print(N[i].lower(),end="")
        elif N[i] == N[i].lower():
            print(N[i].upper(),end="")