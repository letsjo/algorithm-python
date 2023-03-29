# 별 찍기 - 2

N = int(input())

for i in range(N):
    print('{0}{1}'.format(' '*(N-i-1), '*'*(i+1)))
