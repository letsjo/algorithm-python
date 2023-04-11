# 일곱 난쟁이

height = [int(input()) for _ in range(9)]

find = False
sumHeight = sum(height)

for i in range(0, 8):
    for j in range(i+1, 9):
        if (sumHeight-height[i]-height[j] == 100):
            height = height[:j]+height[j+1:]
            height = height[:i]+height[i+1:]
            find = True
            break
    if (find):
        break

height.sort()

for i in height:
    print(i)

# 조합 라이브러리 사용해보기

# import itertools
# height = [int(input()) for _ in range(9)]

# heightCombination = itertools.combinations(height, 7)

# for heightList in heightCombination:
#     if sum(heightList) == 100:
#         print(*sorted(heightList), sep='\n')
#         break
