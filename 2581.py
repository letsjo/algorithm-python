# 소수

import math


def solution(number):
    array = [True for i in range(number + 1)]
    array[0] = False
    array[1] = False
    for i in range(2, int(math.sqrt(number)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= number:
                array[i * j] = False
                j += 1

    return array


M = int(input())
N = int(input())

array = solution(N)
arr_result = []

for i in range(M, N+1):
    if array[i]:
        arr_result.append(i)

if (len(arr_result) == 0):
    print(-1)
else:
    print(sum(arr_result))
    print(arr_result[0])
