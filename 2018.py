# 수들의 합 5

N = int(input())

start = 1
end = 1

count = 0
sum = 1
while start <= N:
    if sum == N:
        sum -= start
        count += 1
        start += 1
    elif sum < N:
        end += 1
        sum += end
    else:
        sum -= start
        start += 1

print(count)
