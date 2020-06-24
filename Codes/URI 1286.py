dp = None
V = None
W = None


def knapsack(N, P):
    if N == 0 or P == 0:
        return 0

    if dp[N][P] == 0:
        if P >= W[N]:
            dp[N][P] = max(V[N] + knapsack(N-1, P-W[N]), knapsack(N - 1, P))
        else:
            dp[N][P] = knapsack(N-1, P)

    return dp[N][P]


while True:
    N = int(input())
    if N == 0:
        break
    P = int(input())
    dp = [[0 for _ in range(P+1)] for _ in range(N+1)]
    V = [0]
    W = [0]
    for _ in range(N):
        val, weight = map(int, input().split())
        V.append(val)
        W.append(weight)

    print(knapsack(N, P), "min.")
