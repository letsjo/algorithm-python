# 가장 긴 증가하는 부분 수열

# Dynamic Programming

# N = int(input())
# A = list(map(int, input().split()))

# dp = [1 for _ in range(N)]

# for i in range(N):
#     for j in range(i):
#         if A[i] > A[j]:
#             dp[i] = max(dp[i], dp[j]+1)

# print(dp)

# Binary Search, Stack

N = int(input())
A = list(map(int, input().split()))

stack = []


def binarySearch(arr, start, end, target):
    if (start >= end):
        return start
    mid = (start + end) // 2

    if (arr[mid] == target):
        return mid
    if (arr[mid] < target):
        return binarySearch(arr, mid+1, end, target)
    return binarySearch(arr, start, mid, target)


for a in A:
    if not stack or (stack[-1] < a):
        stack.append(a)
    else:
        i = binarySearch(stack, 0, len(stack), a)
        stack[i] = a

print(len(stack))
