ans = [5]*50001
for i in range(1,224):
    ans[i**2] = 1
for i in range(1,50001):
    for j in range(1,int(i**(0.5)+1)):
        ans[i] = min(ans[i],ans[i-j*j]+ans[j*j])
print(ans[int(input())])