n = int(input())
m = int(input())
s = input()
k = 0
ans = 0
for i in range(m):
    if k%2:
        if s[i]=='O':k += 1
        else: k = 1
    else:
        if s[i] == 'I':
            k += 1
            if k == 2*n+1:k-=2;ans+=1
        else: k = 0
print(ans)