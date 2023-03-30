# 별 찍기 - 7

N = int(input())

for i in range(N):
    print(' '*(N-i-1)+'*'*i+'*'+'*'*i)

for i in range(N-1):
    print(' '*(i+1)+'*'*(N-i-2)+'*'+'*'*(N-i-2))
