def go(seme_idx, major_gpa, total_gpa):
    if seme_idx + n == 8:
        if major_gpa >= 66 and total_gpa >= 130:
            print('Nice')
            exit()
        return
    for i in range(semester[seme_idx][0] + 1):
        go(seme_idx + 1, major_gpa + 3 * i, total_gpa + 3 * (min(6 - i, semester[seme_idx][1]) + i))

n, a, b = map(int, input().split())
semester = [[*map(int, input().split())] for _ in range(10)]
go(0, a, b)
print('Nae ga wae')