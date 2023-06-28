# 거의 소수
import sys
input = sys.stdin.readline

# 에라토스테네스의 체
def eratos(n):
    primes = [True] * (n+1)
    primes[0], primes[1] = False, False
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i+i, n+1, i):
                primes[j] = False
    return primes

a, b = map(int, input().split())
end = int(b**0.5)+1
arrPrime = eratos(end)
count = 0

for i in range(2, end):
    if arrPrime[i]:
        n = i*i
        while n<=b:
            if a<=n:
                count+=1
            n *= i

print(count)

# 시간 초과 -> 에라토스테네스의 체를 써야한다.
# a, b = map(int,input().split())
# start = int(a**(1/2))
# end = int(b**(1/2))+1

# def isPrime(number):
#     if (number < 2):
#         return False
#     i = 2
#     while (i*i <= number):
#         if (number % i == 0):
#             return False
#         i += 1
#     return True

# count=0
# for i in range(2, end):
#     if isPrime(i):
#         n = i*i
#         while n<=b:
#             if a<=n:
#                 count+=1
#             n *= i

# print(count)