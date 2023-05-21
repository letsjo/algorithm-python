# 어두운 굴다리

n = int(input())
m = int(input())
lights = list(map(int, input().split()))
last = lights[0]
height = lights[0]

for i in range(1,len(lights)):
    tmp = abs(last-lights[i])
    if tmp % 2 == 0:
        tmp = tmp//2
    else:
        tmp = (tmp//2) + 1  
    height = max(height, tmp)
    last = lights[i]

heights = max(height, abs(n-lights[len(lights)-1]))

print(heights)