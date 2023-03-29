# X보다 작은 수

N, X = map(int, input().split(' '))
numbers = list(map(int, input().split(' ')))
count = 0

for number in numbers:
    if (number < X):
        print(number, end=' ')
