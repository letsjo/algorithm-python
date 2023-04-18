# 크게 만들기

N, K = map(int, input().split())
numbers = []
count = K

for a in input().strip():  # 123
    a = int(a)
    while numbers and a > numbers[-1] and count > 0:
        count -= 1
        numbers.pop()
    numbers.append(a)

for i in range(N-K):
    print(numbers[i], end='')
