# Z

N, r, c = map(int, input().split())
# 사각형 크기: 2**N * 2**N  / 2x2 > 4x4 > 8x8
# r 행  c 열 = > (c,r)

# n       = 1 >  2 >  3 >   4 >    5
# x(2**n) = 2 >  4 >  8 >  16 >   32
# y(2**n) = 2 >  4 >  8 >  16 >   32
# c(x*y)  = 4 > 16 > 64 > 256 > 1024

# find(2,3,1)
# N 2 / r 3 / c 1
# 11


def findPointer(n, x, y):
    if (n == 0):
        return 0
    return 2*(x % 2)+(y % 2)+4*findPointer(n-1, x//2, y//2)


print(findPointer(N, r, c))
