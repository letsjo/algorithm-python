# 약수들의 합

while True:
    n = int(input())
    if (n == -1):
        break
    sum = 1
    result = f'{n} = 1'
    for i in range(2, n):
        if (n % i == 0):
            sum += i
            result += f' + {i}'
    if (sum == n):
        print(result)
    else:
        print(f'{n} is NOT perfect.')
