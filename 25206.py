# 너의 평점은

scoresList = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
              'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
sumGrade = 0
sumScore = 0

while True:
    try:
        subject, grade, level = map(str, input().split())
    except:
        break

    if (level == 'P'):
        continue

    grade = float(grade)
    sumGrade += grade
    sumScore += grade * scoresList[level]

print(sumScore/sumGrade)
