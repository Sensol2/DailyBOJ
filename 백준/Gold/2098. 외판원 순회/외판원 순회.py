import math


def tsp(last, visited):
    if visited == (1 << N)-1:  # 모두 방문했다면
        if W[last][0]:  # 돌아갈 수 있는 경로가 있으면
            return W[last][0]
        return math.inf  # 없으면 INF 반환

    if DP[last][visited]:  # DP에 값이 있으면
        return DP[last][visited]

    cost = math.inf
    for i in range(N):
        # 방문하지 않았고, 갈 수 있는 경로라면
        if visited & (1 << i) == 0 and W[last][i] != 0:
            cost = min(cost, tsp(i, visited | (1 << i)) + W[last][i])
    DP[last][visited] = cost
    return cost


N = int(input())
W = [[0] * N for i in range(N)]
DP = [[0] * (1 << N) for _ in range(N)]
for i in range(N):
    W[i] = list(map(int, input().split()))

print(tsp(0, 1))
