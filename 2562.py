# 최댓값
import sys
# 1
# 2
# 3
lines = sys.stdin.readlines()
# print(lines) # ['1\n', '2\n', '3\n']
numbers = list(map(lambda s: int(s.strip()), lines))
# print(numbers)  # ['1', '2', '3']
print(max(numbers), numbers.index(max(numbers))+1, sep='\n')


# import sys

# numbers = list(map(int, sys.stdin.readlines()))
# print(max(numbers), numbers.index(max(numbers))+1, sep='\n')
