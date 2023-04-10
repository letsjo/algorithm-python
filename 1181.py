# 단어 정렬

stringList = [[] for _ in range(51)]

for _ in range(int(input())):
    string = input()
    if string not in stringList[len(string)]:
        stringList[len(string)].append(string)

for index in range(51):
    if (len(stringList[index]) > 0):
        stringList[index].sort()
        for string in stringList[index]:
            print(string)
