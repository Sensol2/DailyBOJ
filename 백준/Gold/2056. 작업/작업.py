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


N = int(input())
indegree = [0] * (N+1)
graph = [[] for i in range(N+1)]
buildTime = [0] * (N+1)
DP = [0] * (N+1)
for i in range(1, N+1):
    items = list(map(int, input().split()))
    # t: i번째 건물의 건설시간
    t = items[0]
    DP[i] = t
    buildTime[i] = t

    # preReqBuilds: i 번째 건물의 선행건물들
    preReqBuilds = items[2:len(items)]
    for builds in preReqBuilds:
        graph[builds].append(i)
        indegree[i] += 1

res = TopologicalSort()

# 위상정렬 순서에 따라 다이나믹 프로그래밍
for r in res:
    for edge in graph[r]:  # 연결된 모든 정점
        if DP[edge] < DP[r] + buildTime[edge]:  # 건설 시간 누적 갱신
            DP[edge] = DP[r] + buildTime[edge]

print(max(DP))
