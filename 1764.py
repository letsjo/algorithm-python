# 듣보잡

N, M = map(int,input().split())

notSaw = {}
notHeard = {}
answers = []

for _ in range(N):
    notSaw[input()] = 1

for _ in range(M):
    tmp = input()
    if tmp in notSaw:
        answers.append(tmp)

answers.sort()
print(len(answers))

for answer in answers:
    print(answer)
