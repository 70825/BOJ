a = int(input())
if 1 <= a <= 1000000000:
    for i in range(10 ** 9):
        if a == 1:
            print("1")
            break
        elif a >= 2:
            if 3 * (i-2) * (i-1) + 1 < a <= 3 * i * (i-1) + 1:
                print(i)
                break
            else:
                continue