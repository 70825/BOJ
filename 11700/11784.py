while 1:
    try:
        S = str(input());s = 0;D = []
        for i in range(len(S) // 2): D.append(int(S[s] + S[s + 1], 16));s += 2
        for i in range(len(D)): print(chr(D[i]), end="")
        print("")
    except EOFError:break