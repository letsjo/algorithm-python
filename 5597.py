# 과제 안 내신 분..?

students = [str(i+1) for i in range(30)]

for i in range(28):
    n = int(input())
    students[n-1] = ''

for student in students:
    if student != '':
        print(student)
