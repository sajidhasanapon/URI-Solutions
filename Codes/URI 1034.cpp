#include <bits/stdc++.h>
#define INF 9999999

using namespace std;

int main()
{
  int T, N, M;
  int coins[26];
  int dp[1000001];

  scanf("%d", &T);

  while(T--)
  {
    scanf("%d %d", &N, &M);
    memset(dp, INF, sizeof(dp));
    dp[0] = 0;

    for(int i = 0; i < N; i++)
    {
      scanf("%d", &coins[i]);
    }
    sort(coins, coins + N);

    for(int i = 0; i < N; i++)
    {
      int c = coins[i];
      for(int j = c; j <= M; j++)
      {
        dp[j] = min(dp[j], dp[j - c] + 1);
      }
    }

    printf("%d\n", dp[M]);
  }

  return 0;
}