n, k = map(int, input().split())
arr = [*map(int, input().split())]
val = [[] for _ in range(k+1)] # 처음 나오는 인덱스 번호, 몇 번 사용하는지
use = [-1 for _ in range(n)] # val[use[i]]로 접근함
ans = 0

for i in range(k-1, -1, -1):
    val[arr[i]].append(i)

for i in range(k):
    flag = False # 이미 있으면 True
    use_flag = False # 다 사용한 제품이면 True
    not_flag = False # 아직 사용안한 멀티탭
    idx = 0
    for j in range(n):
        if arr[i] == use[j]:
            val[use[j]].pop()
            flag = True
            break
        elif not_flag: continue
        elif use[j] == -1:
            not_flag = True
            idx = j
        elif use_flag: continue
        elif len(val[use[j]]) == 0:
            use_flag = True
            idx = j
        elif val[use[j]][-1] > val[use[idx]][-1]: idx = j
    if not flag:
        if not not_flag: ans += 1
        use[idx] = arr[i]
        val[use[idx]].pop()
print(ans)