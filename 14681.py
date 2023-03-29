# 사분면 고르기

numbers = [int(input()) for _ in range(2)]

if (numbers[0] > 0):
    if (numbers[1] > 0):
        print(1)
    else:
        print(4)
else:
    if (numbers[1] > 0):
        print(2)
    else:
        print(3)
