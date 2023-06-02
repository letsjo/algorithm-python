# 집합의 표현 
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m = map(int,input().split())
numbers = [i for i in range(n+1)]

def find_parent(numbers, x):
    if numbers[x] != x:
        numbers[x] = find_parent(numbers, numbers[x])
    return numbers[x]

def union_parent(numbers, a, b):
    a = find_parent(numbers, a)
    b = find_parent(numbers, b)
    if a < b:
        numbers[b] = a
    else:
        numbers[a] = b

for _ in range(m):
    command, a, b = map(int,input().split())
    if command == 0:
        union_parent(numbers, a, b)
    elif command == 1:
        if find_parent(numbers, a) == find_parent(numbers, b):
            print("YES")
        else:
            print("NO")
