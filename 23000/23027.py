S = [*input()]
arr = ['A', 'B', 'C', 'D', 'F']
for i in range(3):
    if arr[i] in S:
        for j in range(len(S)):
            if S[j] in arr[i+1:]: S[j] = arr[i]
        break
else:S = ['A'] * len(S)
print(''.join(S))