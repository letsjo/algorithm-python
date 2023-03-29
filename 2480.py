# 주사위 세개

numbers = list(map(int, input().split()))

if (numbers[0] == numbers[1] & numbers[1] == numbers[2]):
    print(10000+numbers[0]*1000)
elif ((numbers[0] == numbers[1]) | (numbers[0] == numbers[2])):
    print(1000+numbers[0]*100)
elif (numbers[1] == numbers[2]):
    print(1000+numbers[1]*100)
else:
    print(max(numbers)*100)
