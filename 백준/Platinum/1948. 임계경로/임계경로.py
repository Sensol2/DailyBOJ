from collections import deque
import sys

input = sys.stdin.readline


def TopologicalSort():
    result = []
    # 시작 도시를 큐에 추가
    Q = deque()
    Q.append(startCity)

    while Q:
        node = Q.popleft()
        result.append(node)

        for i in graph[node]:
            # 현 노드와 연결된 노드들의 진입차수에서 1 빼기
            indegree[i] -= 1
            # 최대 cost 누적
            DP[i] = max(DP[i], DP[node] + costs[node][i])
            if indegree[i] == 0:  # 새롭게 진입차수 0인 정점 추가
                Q.append(i)

    # 도착 도시를 큐에 추가 (역추적)
    cnt = 0
    Q = deque()
    Q.append(endCity)
    visisted = [False] * (n+1)
    while Q:
        node = Q.popleft()
        for i in back_graph[node]:
            if DP[node] - costs[node][i] == DP[i]:
                cnt += 1
                if not visisted[i]:
                    visisted[i] = True
                    Q.append(i)
    return cnt


n = int(input())  # 도시의 개수
m = int(input())  # 도로의 개수

graph = [[]*(n+1) for _ in range(n+1)]
back_graph = [[]*(n+1) for _ in range(n+1)]
indegree = [0]*(n+1)
costs = [[0]*(n+1) for _ in range(n+1)]
DP = [0]*(n+1)

for i in range(m):
    start, end, t = map(int, input().split())
    graph[start].append(end)
    back_graph[end].append(start)
    indegree[end] += 1
    costs[start][end] = t
    costs[end][start] = t
startCity, endCity = map(int, input().split())


cnt = TopologicalSort()
print(max(DP))
print(cnt)
