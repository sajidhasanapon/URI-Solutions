dp = None
V = None
W = None


def knapsack(N, M):
    if N == 0 or M == 0:
        return 0

    if dp[N][M] == 0:
        if M >= W[N]:
            dp[N][M] = max(V[N] + knapsack(N - 1, M - W[N]), knapsack(N - 1, M))
        else:
            dp[N][M] = knapsack(N - 1, M)

    return dp[N][M]


while True:
    N = int(input())
    if N == 0:
        break
    V = [0]
    W = [0]
    for _ in range(N):
        val, weight = map(int, input().split())
        V.append(val)
        W.append(weight)
    M = int(input())
    dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    print(knapsack(N, M))
