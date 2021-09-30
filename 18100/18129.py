S, K = input().split()
S = [*S]
K = int(K)
for i in range(len(S)): S[i]=S[i].upper()

ans = []
val = [S[0], 1]
visit = []
for i in range(1, len(S)):
    if S[i] in visit: continue
    if val[0] == S[i]: val[1] += 1
    else:
        ans += [0] if val[1] < K else [1]
        visit += val[0]
        val = [S[i], 1]
if val[0] not in visit: ans += [0] if val[1] < K else [1]
print(''.join(map(str,ans)))