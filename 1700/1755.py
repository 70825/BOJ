arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
m, n = map(int, input().split())
values = []
numbers = [(i-m, i) for i in range(m, n+1)]
for i in range(m, n+1):
    if i < 10: values.append(arr[i])
    else: values.append(arr[i//10]+' '+arr[i%10])
numbers.sort(key= lambda x: values[x[0]])
for i in range((n - m + 1)//10 + (1 if (n - m + 1) % 10 else 0)):
    ans = [numbers[j][1] for j in range(i*10, min(len(numbers), (i+1)*10))]
    print(*ans)