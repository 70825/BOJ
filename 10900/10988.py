N =input()
k = 0
for i in range(len(N)//2):
    if N[i] == N[len(N)-1-i]:
        continue
    else:
        k += 1
if k > 0:
    print("0")
else:
    print("1")