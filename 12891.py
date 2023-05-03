# DNA 비밀번호
from collections import deque

S, P = map(int, input().split())

DNA = input()

alphaIndex = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
limit = list(map(int, input().split()))

password = deque()
count = 0

for i in range(len(DNA)):
    password.append(DNA[i])
    if DNA[i] in ['A', 'C', 'G', 'T']:
        limit[alphaIndex[DNA[i]]] -= 1

    if len(password) == P:
        if limit[0] <= 0 and limit[1] <= 0 and limit[2] <= 0 and limit[3] <= 0:
            count += 1
        alphaPop = password.popleft()
        if alphaPop in ['A', 'C', 'G', 'T']:
            limit[alphaIndex[alphaPop]] += 1


print(count)
