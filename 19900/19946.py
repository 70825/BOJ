n = int(input())
for i in range(65):
    val = 2 ** i - 1
    for j in range(i+1, 65):
        val *= 2
    if val == n:
        print(i)