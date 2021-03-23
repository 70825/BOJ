n = int(input())
s = input()
D = {'000000':'A', '001111':'B', '010011':'C','011100':'D','100110':'E','101001':'F','110101':'G','111010':'H'}
ans = ''
for i in range(0,len(s),6):
    z = s[i:i+6]
    score = [0]*8
    for j,x in enumerate(D.keys()):
        for k in range(len(x)):
            if z[k] == x[k]: score[j] += 1
    if max(score) >= 5:
        for j in range(8):
            if score[j] == max(score):
                ans += D[list(D.keys())[j]]
    else:print(i//6 + 1);exit()
print(ans)