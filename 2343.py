# 기타 레슨

n, m = map(int,input().split())

lesson = list(map(int,input().split()))

start = max(lesson)
end = sum(lesson)

while (start<=end):
    mid = (start+end)//2
    count = 1
    total = 0

    for i in range(n):
        if total+lesson[i] > mid:
            count+=1
            total=0
        total += lesson[i]
    
    if count > m:
        start = mid+1
    else:
        end = mid-1

print(start)

# 구간합으로는 풀이 실패

# n, m = map(int,input().split())

# lesson = list(map(int,input().split()))
# lesson_sum = [0]*(n+1)

# for i in range(1,n+1):
#     lesson_sum[i] += lesson_sum[i-1] + lesson[i-1]

# bluelays = [0]*m
# average = lesson_sum[n] / m
# print(average)
# start = 0
# count = 0

# for i in range(1,n+1):
#     bluelays[count] = lesson_sum[i]-lesson_sum[start]
#     if bluelays[count] > average:
#         sum_2 = lesson_sum[i-1]-lesson_sum[start]
#         if bluelays[count]-average > average-sum_2:
#             bluelays[count] = sum_2
#             bluelays[count+1] = lesson_sum[i] - lesson_sum[i-1]
#             count+=1
#             start = i-1
#         else:
#             count+=1
#             start = i
#     print(count)
# print(bluelays)

# while(bluelays[len(bluelays)-1] == 0):
#     bluelays.pop()
#     bluelays.pop(bluelays.index(max(bluelays)))

# print(bluelays)
# print(max(bluelays))