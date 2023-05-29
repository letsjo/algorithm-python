# 회전하는 큐
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
removes = list(map(int,input().split()))

queue = deque([i for i in range(1,n+1)])
count = 0

for remove in removes:
    while True:
        if queue[0] == remove:
            queue.popleft()
            break
        else:
            if queue.index(remove) <= len(queue) // 2:
                queue.append(queue.popleft())
            else:
                queue.appendleft(queue.pop())
            count += 1
    
print(count)