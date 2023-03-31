# 달팽이는 올라가고 싶다
import math

A, B, V = map(int, input().split())

print(math.trunc((V-A-1)/(A-B)+2))
