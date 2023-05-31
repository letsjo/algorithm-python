# 로프

n = int(input())
rope = []
for _ in range(n):
    rope.append(int(input()))

rope.sort(reverse=True)

answer = 0
for i in range(n):
    answer = max(answer,rope[i]*(i+1))

print(answer)