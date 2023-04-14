# 두 용액

N = int(input())
liquids = sorted(list(map(int, input().split())))
# -99 -2 -1 4 98
start = 0
end = len(liquids)-1
minResult = float('inf')
answer = [liquids[start], liquids[end]]

while start < end:
    result = liquids[start] + liquids[end]
    absResult = abs(result)
    if (minResult > absResult):
        minResult = min(minResult, absResult)
        answer = [liquids[start], liquids[end]]
        if (result == 0):
            break
    if (result > 0):
        end -= 1
    else:
        start += 1

print(answer[0], answer[1])
