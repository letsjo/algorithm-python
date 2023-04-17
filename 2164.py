# 카드2

import sys
input = sys.stdin.readline
N = int(input())


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


queue = Queue()
for i in range(N):
    queue.push(i+1)

while queue.size() != 1:
    queue.pop()
    queue.push(queue.pop())

print(queue.front())
