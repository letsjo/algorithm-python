# 소수 찾기

def isPrime(number):
    if (number < 2):
        return False
    i = 2
    while (i*i <= number):
        if (number % i == 0):
            return False
        i += 1
    return True


T = int(input())
count = 0
for n in list(map(int, input().split())):
    if (isPrime(n)):
        count += 1

print(count)
