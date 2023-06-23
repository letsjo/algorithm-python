# 두 수의 합
import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int,input().split()))
numbers.sort()

x = int(input())

start = 0
end = len(numbers) - 1
count = 0

while(start<end):
    sum = numbers[start]+numbers[end]

    if sum == x:
        count+=1

    if (sum>=x):
        end -= 1
    else:
        start += 1

print(count)
