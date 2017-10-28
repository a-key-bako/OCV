# 蟻本 p.35 全探索 - 深さ優先探索
N, M = 0, 0
field = [[0 for _i in range(100)] for _j in range(100)]

dxy_list = [-1, 0, 1]

def dfs(x, y):
    field[x][y] = "."
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            nx, ny = x + dx, y + dy
            if 0 <= nx and nx < N and 0 <= ny and ny < M and field[nx][ny] == "W":
                dfs(nx, ny)
    return None

def solve():
    res = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == "W":
                dfs(i, j)
                res += 1
    print(res)


# input
N = int(input())
M = int(input())
for i in range(N):
    l = input()
    for j, c in enumerate(l):
        field[i][j] = c

solve()
