# 蟻本 p.60 動的計画法
P_INF = float("inf")
N_MAX = 100
M_MAX = 100

def solve():
    n = int(input())
    w = [0 for i in range(n)]
    v = [0 for i in range(n)]
    for i in range(n):
        w[i], v[i] = list(map(int, input().split()))
    W = int(input())
    
    dp = [[P_INF for i in range(N_MAX*M_MAX+1)] for j in range(N_MAX+1)]
    dp[0][0] = 0
    
    for i in range(n):
        for j in range(N_MAX*M_MAX+1):
            if j < v[i]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = min(dp[i][j], dp[i][j-v[i]]+w[i])
    ans = 0
    for i in range(N_MAX*M_MAX+1):
        if dp[n][i] <= W:
            ans = i
    print(ans)

solve()

"""
sample input 1
4
2 3
1 2
3 4
2 2
5

sample output 1
7
"""
