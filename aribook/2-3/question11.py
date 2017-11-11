# 蟻本 p.58 動的計画法
def solve():
    n = int(input())
    w = [0 for i in range(n)]
    v = [0 for i in range(n)]
    for i in range(n):
        w[i], v[i] = list(map(int, input().split()))
    W = int(input())
    
    dp = [[0 for i in range(W+1)] for j in range(n+1)]
    
    for i in range(n):
        for j in range(W+1):
            if j < w[i]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j], dp[i+1][j-w[i]]+v[i])
    print(dp[n][W])

solve()

"""
sample iuput 1
3
3 4
4 5
2 3
7

sample output 1
10
"""
