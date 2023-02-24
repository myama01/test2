for h in range(H + 1):
    dp[i + 1][h] = max(dp[i + 1][h], dp[i][h])
    dp[i + 1][max(h - b, 0)] = max(dp[i + 1][max(h - b, 0)], 
                                   dp[i][h] + a * h)

def func(act1, act2):
    if min(act1[1], act2[1] - act1[0]) \ 
    <= min(act2[1], act1[1] - act2[0]):
        
for j in range(0, K + 1):
    dp[i + 1][j] = (sum_dp[i][j + 1] \
        - sum_dp[i][max(j - a[i], 0)]) % MOD
    
    
while L_lazy < R_lazy:
    if L_lazy & 1:
        self._lazy[L_lazy] = 
        self._combine_lazy_f(self._lazy[L_lazy], value)
        L_lazy += 1
    if R_lazy & 1:
        R_lazy -= 1
        self._lazy[R_lazy] = self._combine_lazy_f(self._lazy[R_lazy], value)
        
        
if len(S2s) > 0:
    dp[S] = min(dp[S], sum(dp[x] for x in S2s) / len(S2s) + 5.0 / len(S2s))
                sum(dp[x] for x in S2s) / len(S2s) + 5.0 / len(S2s))
