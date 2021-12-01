n = int(input())
for i in range(n, -1, -1):
    if i > 1: print(f'{i} bottles of beer on the wall, {i} bottles of beer.')
    elif i == 1: print('1 bottle of beer on the wall, 1 bottle of beer.')
    else: print('No more bottles of beer on the wall, no more bottles of beer.')

    if i >= 3: print(f'Take one down and pass it around, {i-1} bottles of beer on the wall.\n')
    elif i == 2: print('Take one down and pass it around, 1 bottle of beer on the wall.\n')
    elif i == 1: print('Take one down and pass it around, no more bottles of beer on the wall.\n')
    elif n == 1: print(f'Go to the store and buy some more, {n} bottle of beer on the wall.')
    else: print(f'Go to the store and buy some more, {n} bottles of beer on the wall.')