# 한수

def isHansu(number):
    numberWord = str(number)
    for index in range(0, len(numberWord)-2):
        gap1 = int(numberWord[index+2]) - int(numberWord[index+1])
        gap2 = int(numberWord[index+1]) - int(numberWord[index])
        if (gap1 != gap2):
            return False
    return True


N = int(input())
if (N < 99):
    print(N)
elif (N < 111):
    print(99)
else:
    answer = 99
    for case in range(111, N+1):
        if (isHansu(case)):
            answer += 1
    print(answer)
