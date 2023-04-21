# 최소 스패닝 트리
V, E = map(int, input().split())

# 노드 초기화
parent = [0] * (V+1)
for i in range(1, V+1):
    parent[i] = i

# 간선 초기화
edges = []
answer = 0

for _ in range(E):
    a, b, weight = map(int, input().split())
    edges.append((weight, a, b))

edges.sort()

# parent - 부모값 리스트, x - 현재값 부모


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 작은 값이 부모로 만들기


def union_parent(parent, a, b):
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(E):
    # 가중치가 작은값부터 하나씩 꺼내기
    weight, a, b = edges[i]
    a_parent = find_parent(parent, a)
    b_parent = find_parent(parent, b)
    if a_parent != b_parent:
        union_parent(parent, a_parent, b_parent)
        answer += weight

print(answer)
