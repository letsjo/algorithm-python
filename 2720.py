# 세탁소 사장 동혁

T = int(input())
coins = [25, 10, 5, 1]

for _ in range(T):
    change = int(input())
    for coin in coins:
        print(change//coin, end=' ')
        change %= coin
    print()
