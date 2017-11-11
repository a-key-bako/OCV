# 蟻本 p.52 動的計画法
def solve():
    N = int(input())
    w = [0 for i in range(N)]
    v = [0 for i in range(N)]
    for i in range(N):
        w[i], v[i] = list(map(int, input().split()))
    W = int(input())
    
    dp = [[0 for i in range(W+1)] for j in range(N+1)]
    
    for i in range(N):
        for j in range(W+1):
            if j < w[i]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j], dp[i][j-w[i]]+v[i])
    print(dp[N][W])

solve()

"""
sample iuput 1
4
2 3
1 2
3 4
2 2
5

sample output 1
7
"""
