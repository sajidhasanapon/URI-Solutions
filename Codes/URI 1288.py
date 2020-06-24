dp = None
V = None
W = None


def knapsack(N, K):
    if N == 0 or K == 0:
        return 0

    if dp[N][K] == 0:
        if K >= W[N]:
            dp[N][K] = max(V[N] + knapsack(N-1, K-W[N]), knapsack(N - 1, K))
        else:
            dp[N][K] = knapsack(N-1, K)

    return dp[N][K]


T = int(input())
for _ in range(T):
    N = int(input())
    V = [0]
    W = [0]
    for _ in range(N):
        X, Y = map(int, input().split())
        V.append(X)
        W.append(Y)

    K = int(input())
    R = int(input())

    dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

    res = knapsack(N, K)
    print("Missao completada com sucesso") if res >= R else print("Falha na missao")
