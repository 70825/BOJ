n, m = map(int, input().split())
A, B = input().split()
count = [3, 2, 1, 2, 4,3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
arr = []
for i in range(min(len(A), len(B))):
    arr.append(count[ord(A[i])-ord('A')])
    arr.append(count[ord(B[i])-ord('A')])
if len(A) > len(B):
    for i in range(len(B), len(A)):
        arr.append(count[ord(A[i])-ord('A')])
if len(B) > len(A):
    for i in range(len(A), len(B)):
        arr.append(count[ord(B[i])-ord('A')])
while len(arr) != 2:
    new_arr = []
    for i in range(1, len(arr)):
        new_arr.append((arr[i] + arr[i-1]) % 10)
    arr = new_arr
print(str(arr[0]*10+arr[1])+"%")