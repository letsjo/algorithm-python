# 뱀

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

    def push_front(self, value):
        self.stackOldest.append(value)

    def __shiftStacks(self):
        if len(self.stackOldest) == 0:
            while len(self.stackNewest) > 0:
                self.stackOldest.append(self.stackNewest.pop())

    def pop(self):
        self.__shiftStacks()
        return self.stackOldest.pop()

    def pop_back(self):
        self.__shiftStacks()
        if len(self.stackNewest) == 0:
            if (len(self.stackOldest) == 1):
                return self.stackOldest.pop()
            elif (len(self.stackOldest) == 0):
                return None
            while len(self.stackOldest) != 1:
                self.stackNewest.append(self.stackOldest.pop())
            return self.stackOldest.pop()
        else:
            return self.stackNewest.pop()

    def front(self):
        self.__shiftStacks()
        if len(self.stackOldest) != 0:
            return self.stackOldest[len(self.stackOldest)-1]
        else:
            return self.stackNewest[0]

    def back(self):
        self.__shiftStacks()
        if len(self.stackOldest) != 0:
            return self.stackOldest[0]
        elif len(self.stackNewest) != 0:
            return self.stackNewest[len(self.stackNewest)-1]
        else:
            return None


class Snake:
    def __init__(self, y, x, dir):
        self.position = Queue()
        self.position.push([y, x, dir])

    def pushFront(self, y, x, dir):
        self.position.push_front([y, x, dir])

    def push(self, y, x, dir):
        self.position.push([y, x, dir])

    def popFront(self):
        return self.position.pop()

    def popBack(self):
        return self.position.pop_back()

    def front(self):
        [y, x, dir] = self.position.front()
        return {'x': x, 'y': y, 'dir': dir}

    def back(self):
        [y, x, dir] = self.position.back()
        return {'x': x, 'y': y, 'dir': dir}


N = int(input())
K = int(input())

dummyMap = [[0 for _ in range(N+1)] for _ in range(N+1)]
visit = [[0 for _ in range(N+1)] for _ in range(N+1)]
live = True
answer = 0
snake = Snake(1, 1, 0)

for i in range(K):
    y, x = map(int, input().split())
    dummyMap[y][x] = 1

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

prev = 0


def turnLeft(direction):
    if (direction == 3):
        return 0
    return direction+1


def turnRight(direction):
    if (direction == 0):
        return 3
    return direction-1


def move(timer, direction):
    global answer
    for _ in range(timer):
        answer += 1
        head = snake.front()
        yy = head['y'] + dy[head['dir']]
        xx = head['x'] + dx[head['dir']]
        if (1 <= yy and yy <= N and 1 <= xx and xx <= N and visit[yy][xx] == 0):
            if dummyMap[yy][xx] == 1:
                snake.pushFront(yy, xx, head['dir'])
                dummyMap[yy][xx] = 0
            else:
                snake.pushFront(yy, xx, head['dir'])
                tail = snake.back()
                visit[tail['y']][tail['x']] = 0
                snake.popBack()
            visit[yy][xx] = 1
        else:
            return False

    now = snake.front()
    if (direction == 'L'):
        now['dir'] = turnLeft(now['dir'])
    elif (direction == 'D'):
        now['dir'] = turnRight(now['dir'])

    snake.popFront()
    snake.pushFront(now['y'], now['x'], now['dir'])

    return True


L = int(input())
for _ in range(L):
    timer, direct = input().split()
    timer = int(timer)

    if (move(timer-prev, direct) == False):
        live = False
        break
    prev = timer

if (live):
    while True:
        answer += 1
        head = snake.front()
        yy = head['y'] + dy[head['dir']]
        xx = head['x'] + dx[head['dir']]
        if (1 <= yy and yy <= N and 1 <= xx and xx <= N and visit[yy][xx] == 0):
            if (dummyMap[yy][xx] == 1):
                snake.pushFront(yy, xx, head['dir'])
                dummyMap[yy][xx] = 0
            else:
                snake.pushFront(yy, xx, head['dir'])
                tail = snake.back()
                visit[tail['y']][tail['x']] = 0
                snake.popBack()
            visit[yy][xx] = 1
        else:
            break
print(answer)
