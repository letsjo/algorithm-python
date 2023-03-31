# 평균은 넘겠지

C = int(input())

for _ in range(C):
    line = list(map(int, input().split()))
    N = line[0]
    average = sum(line[1:]) / N
    percent = len([score for score in line[1:] if score > average]) / N * 100
    print(f"{percent:.3f}%")
