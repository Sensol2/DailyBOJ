from collections import deque
import sys

input = sys.stdin.readline


def TopologicalSort():
    result = []
    # 들어오는 간선이 없는 노드를 큐에 추가
    Q = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:  # 진입차수 0 인 노드 큐에 삽입
            Q.append(i)

    while Q:
        node = Q.popleft()
        result.append(node)

        for i in graph[node]:
            # 현 노드와 연결된 노드들의 진입차수에서 1 빼기
            indegree[i] -= 1
            if indegree[i] == 0:  # 새롭게 진입차수 0인 정점 추가
                Q.append(i)

    return result


N, M = map(int, input().split())
indegree = [0] * (N + 1)
graph = [[] for _ in range(N+1)]
for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

nodes = TopologicalSort()
print(' '.join(map(str, nodes)))
