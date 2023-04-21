# 이진 검색 트리

# import sys
# MAX_NUM = 10000

# input = sys.stdin.readline

# tree = [None] * (MAX_NUM*4)


# def pushNumber(index, number):
#     if tree[index] is None:
#         tree[index] = number
#         return
#     if tree[index] > number:
#         return pushNumber(2*index+1, number)
#     if tree[index] <= number:
#         return pushNumber(2*index+2, number)


# def postOrder(index):
#     if tree[2*index+1] is not None:
#         postOrder(2*index+1)
#     if tree[2*index+2] is not None:
#         postOrder(2*index+2)
#     print(tree[index])
#     return


# n = 0
# while True:
#     try:
#         number = int(input())
#         pushNumber(n, number)
#     except:
#         break

# postOrder(0)

import sys
sys.setrecursionlimit(10000)


class Node:
    def __init__(self, key, value, left, right):
        self.key = KeyboardInterrupt
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree():
    def __init__(self) -> None:
        self.root = None

    def add(self, key, value) -> bool:
        def add_node(node, key, value) -> None:
            if key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
            return True

        if self.root is None:
            self.root = Node(key, value, None, None)
            return True
        else:
            return add_node(self.root, key, value)

    def dump(self):
        def print_subtree(node):
            if node is not None:
                print_subtree(node.left)
                print_subtree(node.right)
                print(f'{node.value}')
        root = self.root
        print_subtree(root)

    def remove(self, key) -> bool:
        node = self.root
        parent = None
        is_left_child = True

        while True:
            if node is None:
                return False
            if key == node.key:
                break
            else:
                parent = node
                if key < node.key:
                    node = node.left
                    is_left_child = True
                else:
                    node = node.right
                    is_left_child = False

        if node.left is None:
            if node is self.root:
                self.root = node.right
            elif is_left_child:
                parent.left = node.right
            else:
                parent.right = node.right

        elif node.right is None:
            if node is self.root:
                self.root = node.left
            elif is_left_child:
                parent.left = node.left
            else:
                parent.right = node.left

    def search(self, key) -> int:
        node = self.root
        while True:
            if node is None:
                return -1
            if key == node.key:
                return node.value
            elif key < node.key:
                node = node.left
            else:
                node = node.right


input = sys.stdin.readline

tree = BinarySearchTree()

while True:
    try:
        number = int(input())
        tree.add(number, number)
    except:
        break

tree.dump()
