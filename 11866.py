# 요세푸스 문제 0

import sys
input = sys.stdin.readline


class Queue:
    def __init__(self):
        self.stackNewest = []
        self.stackOldest = []

    def size(self):
        return len(self.stackNewest) + len(self.stackOldest)

    def push(self, value):
        self.stackNewest.append(value)

    def __shiftStacks(self):
        if len(self.stackOldest) == 0:
            while len(self.stackNewest) > 0:
                self.stackOldest.append(self.stackNewest.pop())

    def pop(self):
        self.__shiftStacks()
        return self.stackOldest.pop()

    def front(self):
        self.__shiftStacks()
        return self.stackOldest[len(self.stackOldest)-1]

    def back(self):
        self.__shiftStacks()
        if len(self.stackNewest) == 0:
            return self.stackOldest[0]
        else:
            return self.stackNewest[len(self.stackNewest)-1]


N, K = map(int, input().split())
queue = Queue()
stack = []

for i in range(N):
    queue.push(str(i+1))

while queue.size() > 0:
    for _ in range(K-1):
        queue.push(queue.pop())
    stack.append(queue.pop())
print('<', end='')
print(', '.join(stack), end='>')
