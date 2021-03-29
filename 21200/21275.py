a,b = input().split()
val = {str(i):i for i in range(10)}
val.update({chr(97+i):i+10 for i in range(26)})
A = [[int(a,k),k] for k in range(max(2,max(val[a[i]]+1 for i in range(len(a)))),37)]
B = [[int(b,k),k] for k in range(max(2,max(val[b[i]]+1 for i in range(len(b)))),37)]
ans = [A[i]+[B[j][1]] for j in range(len(B)) for i in range(len(A)) if (A[i][0] == B[j][0] and A[i][1] != B[j][1] and A[i][0] < 2**63)]
print('Impossible') if not len(ans) else print(*ans[0]) if len(ans) == 1 else print('Multiple')