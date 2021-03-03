a =[[0] * 4 for i in range(5)]
s = [0] * 5
for i in range(5):
    a[i][0],a[i][1],a[i][2],a[i][3] = map(int,input().split())
    s[i] = sum(a[i])
for i in range(5):
    if max(s) == s[i]:
        print(i+1,max(s))
        break