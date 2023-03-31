# 소수 찾기
import math


def isPrime(number):
    if (number < 2):
        return False
    for i in range(2, math.ceil(number/2)+1):
        if (number % i == 0):
            return False
    return True


T = int(input())
count = 0
for n in list(map(int, input().split())):
    if (isPrime(n)):
        count += 1

print(count)
