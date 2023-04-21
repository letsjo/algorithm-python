# 트리 순회

N = int(input())

tree = {}

for _ in range(N):
    root, left, right = input().rstrip().split()
    tree[root] = [left, right]


def printTree(root, type):
    if root == '.':
        return
    if (type == 'pre'): print(root, end='')
    printTree(tree[root][0],type)
    if (type == 'in'): print(root, end='')
    printTree(tree[root][1],type)
    if (type == 'post'): print(root, end='')


printTree('A','pre')
print()
printTree('A','in')
print()
printTree('A','post')
