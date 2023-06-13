# 신기한 소수

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

n = int(input())

def isPrime(number):
    if (number < 2):
        return False
    i = 2
    while (i*i <= number):
        if (number % i == 0):
            return False
        i += 1
    return True

def dfs(number, count):
    if (count == n):
        print(number)
        return
    for i in range(1,10):
        if (isPrime(number*10+i)):
            dfs(number*10+i, count+1)

for i in range(2,10):
    if (isPrime(i)):
        dfs(i,1)
