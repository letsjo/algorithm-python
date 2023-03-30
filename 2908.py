# 상수

A, B = map(str, input().split())

reverseA = int(''.join(list(reversed(A))))
reverseB = int(''.join(list(reversed(B))))

print(reverseA if (reverseA > reverseB) else reverseB)
