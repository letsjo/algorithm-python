# 빠른 A+B
import sys

input = sys.stdin.readline
T = int(input())

for i in range(T):
    input_data = input().rstrip().split(' ')
    A = int(input_data[0])
    B = int(input_data[1])
    print(A+B)
