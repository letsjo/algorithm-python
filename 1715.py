# 카드 정렬하기
import sys
import heapq
input = sys.stdin.readline

N = int(input())
deck = []

for _ in range(N):
    heapq.heappush(deck, int(input()))

sum = 0

while len(deck) > 1:
    mixedDeck = heapq.heappop(deck) + heapq.heappop(deck)
    sum += mixedDeck
    heapq.heappush(deck, mixedDeck)

print(sum)
