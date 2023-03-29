year = int(input())

isMultipleFour = year % 4 == 0
isMultipleOneHundredOrFourHundred = (year % 100 != 0) | (year % 400 == 0)

if (isMultipleFour & isMultipleOneHundredOrFourHundred):
    print(1)
else:
    print(0)
