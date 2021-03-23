n = int(input())
arr = list(map(int, input().split()))
ans1, ans2 = 0, 0 #각각 영식, 민식 요금제 총 금액
for i in range(n):
    #영식 요금제
    x = arr[i] // 30
    ans1 += 10 * x + 10
    #민식 요금제
    y = arr[i] // 60
    ans2 += 15 * y + 15

if ans1 == ans2:
    print('Y','M',ans1)
elif ans1 > ans2: #민식 요금제가 더 쌈
    print('M',ans2)
else: #영식 요금제가 더 쌈
    print('Y',ans1)