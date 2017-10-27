# p.34 全探索 - 深さ優先探索
a = [0 for i in range(100000)]
n, k = 0, 0

def dfs(i, sum):
    if i == n:
        return sum == k
    if dfs(i + 1, sum):
        return True
    if dfs(i + 1, sum + a[i]):
        return True
    return False
