# 큐 2

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

for _ in range(N):
    order = input().split()
    if (order[0] == 'push'):
        queue.push(order[1])
    elif (order[0] == 'pop'):
        if (queue.size() == 0):
            print('-1')
        else:
            print(queue.pop())
    elif (order[0] == 'size'):
        print(queue.size())
    elif (order[0] == 'empty'):
        if (queue.size() == 0):
            print('1')
        else:
            print('0')
    elif (order[0] == 'front'):
        if (queue.size() == 0):
            print('-1')
        else:
            print(queue.front())
    elif (order[0] == 'back'):
        if (queue.size() == 0):
            print('-1')
        else:
            print(queue.back())
