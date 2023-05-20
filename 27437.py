# 분수찾기 2 / 이분탐색

X = int(input())
start = 1
end = 10**18

while start < end:
    mid = (start+end)//2
    target = (mid*(mid+1))//2 
    if target < X :
        start = mid+1
    else:
        end = mid

row = start
col = X - (row*(row-1)//2)

if (row % 2 == 0):
    print(f'{col}/{row-col+1}')
else:
    print(f'{row-col+1}/{col}')