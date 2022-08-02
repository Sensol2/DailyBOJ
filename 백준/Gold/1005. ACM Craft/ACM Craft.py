from collections import deque


def TopologicalSort(PrereqTech):
    result = []
    # 들어오는 간선이 없는 노드를 큐에 추가
    Q = deque()
    visisted = [False] * (N+1)
    while True:
        for i in range(1, N+1):
            if not PrereqTech[i] and not visisted[i]:
                visisted[i] = True
                Q.append(i)
        if Q:
            node = Q.popleft()
            result.append(node)
            for i in range(1, N+1):
                if node in PrereqTech[i]:
                    PrereqTech[i].remove(node)
            continue
        break
    return result


T = int(input())

for i in range(T):
    N, K = map(int, input().split())  # 건물, 규칙순서
    builds = list(map(int, input().split()))  # 건물 당 걸리는 건물 건설시간
    builds.insert(0, 0)

    techTree = [[] for _ in range(N+1)]
    PrereqTech = [[] for _ in range(N+1)]  # i번째 건물 건설에 필요한 선행건물 목록
    for j in range(K):
        first, second = map(int, input().split())
        techTree[first].append(second)
        PrereqTech[second].append(first)
    W = int(input())  # 승리하기 위해 지어야 하는 건물 번호

    nodes = TopologicalSort(PrereqTech[:])  # 위상 정렬
    DP = builds[:]
    for node in nodes:
        for next in techTree[node]:
            if DP[next] < DP[node] + builds[next]:
                DP[next] = DP[node] + builds[next]

    print(DP[W])
