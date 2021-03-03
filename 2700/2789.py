word = str(input())
if 3<= len(word) <= 100 and word == word.upper():
    K = [None] * len(word)
    for i in range(len(word)):
       K[i] = word[i]
       if K[i] == "A" or K[i] == "B" or K[i] == "C" or K[i] == "D" or K[i] == "E" or K[i] == "G" or K[i] == "I" or K[i] == "M" or K[i] == "R":
           K[i] = ""
    for i in range(len(word)):
        print(K[i],end="")