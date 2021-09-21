n, m = map(int, input().split()); n+=1
total_std = [0] * n
blue = [[] for _ in range(n)]
white = [[] for _ in range(n)]
while 1:
    a, b = input().split()
    if a == b == '0': break
    a = int(a)
    if total_std[a] < m:
        total_std[a] += 1
        if a % 2: blue[a].append(b)
        else: white[a].append(b)
for team in [blue, white]:
    for idx, class_val in enumerate(team):
        class_val.sort(key=lambda x:[len(x), x])
        for name in class_val:
            print(idx, name)