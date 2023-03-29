# A+B - 4

import sys

inputs = sys.stdin.readlines()

for input in inputs:
    A, B = map(int, input.split())
    print(A+B)

# while True:
#     try:
#         a, b = map(int, input().split())
#         print(a+b)

#     except:
#         break
