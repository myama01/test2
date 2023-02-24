for h in range(H + 1):
dp[i + 1][h] = max(dp[i + 1][h], dp[i][h])
dp[i + 1][max(h - b, 0)] = max(dp[i + 1][max(h - b, 0)], dp[i][h]
+ a * h)
