# 나머지

answer = []

for _ in range(10):
    rest = int(input()) % 42
    try:
        answer.index(rest)
    except ValueError:
        answer.append(rest)

print(len(answer))
