# s = [list(map(int, input())) for _ in range(2)]
# [[1, 1, 1], [2, 2, 2]]
s = [input() for _ in range(2)]
# ['111', '222']
total = 0
count = 0
number = int(s[0])
s[1] = str(s[1])[::-1]
for i in s[1]:
    sum = number*int(i)
    print(sum)
    total += sum*10**count
    count += 1
print(total)
