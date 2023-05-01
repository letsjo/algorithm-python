# 멀티탭 스케줄링

N, K = map(int, input().split())

orders = list(map(int, input().split()))

supply = [0]*(N)
count = 0

for i in range(K):
    if orders[i] in supply:
        continue
    elif 0 in supply:
        supply[supply.index(0)] = orders[i]
        continue
    count += 1
    pop_index = i
    supply_index = N-1
    for j in range(N):
        if supply[j] in orders[i+1:]:
            tem_index = orders.index(supply[j], i)
            if tem_index > pop_index:
                pop_index = tem_index
                supply_index = j
        else:
            supply_index = j
            break
    supply[supply_index] = orders[i]

print(count)
