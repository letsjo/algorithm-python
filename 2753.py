# 윤년

year = int(input())

# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때
# 또는 400의 배수일 때이다.
isLeapYearCondition1 = year % 4 == 0 and year % 100 != 0
isLeapYearCondition2 = year % 400 == 0

if (isLeapYearCondition1 or isLeapYearCondition2):
    print(1)
else:
    print(0)
