for _ in range(int(input())):
    s = [*input()]
    idx = -1
    for i in range(len(s)//2):
        if s[i] != s[-1-i]:
            idx = i
            break
    if idx == -1:
        print(0)
        continue

    flag = [True, True]
    for i, (x, y) in enumerate([(idx + 1, len(s) - 1 - idx), (idx, len(s) - 2 - idx)]):
        while x <= y:
            if s[x] != s[y]:
                flag[i] = False
                break
            x += 1; y -= 1
    if flag[0] or flag[1]: print(1)
    else: print(2)