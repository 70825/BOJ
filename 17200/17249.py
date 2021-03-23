a,b = input().split('0')
ans = [0, 0]
for i in range(len(a)):
    if a[i] == '@': ans[0]+=1
for i in range(len(b)):
    if b[i] == '@': ans[1]+=1
print(' '.join(map(str,ans)))