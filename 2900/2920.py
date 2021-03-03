a = input()
count = 0
a_list = a.split()
for i in range(1,8):
    if int(a_list[i]) > int(a_list[i-1]) :
        count += 1
    elif int(a_list[i]) < int(a_list[i-1]) :
        count -= 1
if count == 7:
    print("ascending")
elif count == -7:
    print("descending")
else:
    print("mixed")