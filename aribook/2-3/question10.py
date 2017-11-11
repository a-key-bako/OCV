# 蟻本 p.54 動的計画法
def solve():
    n = int(input())
    m = int(input())
    s = input()
    t = input()
    
    dp = [[0 for i in range(n+1)] for j in range(m+1)]
    
    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:
                dp[i+1][j+1] = dp[i][j]+1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    print(dp[n][m])
    
solve()

"""
sample iuput 1
4
4
abcd
becd

sample output 1
3
"""
