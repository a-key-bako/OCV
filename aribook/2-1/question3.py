# 蟻本 p.37 全探索 - 幅優先探索
import queue

INF = 100000000
MAX_N = 100
MAX_M = 100

maze = [[0 for i in range(MAX_N)] for j in range(MAX_M)] # 迷路を表す文字列の配列
N, M = 0, 0
sx, sy = 0, 0 # スタートの座標
gx, gy = 0, 0 # ゴールの座標

d = [[0 for i in range(MAX_N)] for j in range(MAX_M)] # 各点までの最短距離の配列

# 移動4方向のベクトル
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

# (sx, sy)から(gx, gy)への最短距離を求める
# たどり着けないとINF
def bfs():
    que = queue.Queue()
    # すべての点をINFで初期化
    for i in range(N):
        for j in range(N):
            d[i][j] = INF
    # スタート地点をキューに入れて、その点の距離を0にする
    que.put((sx, sy))
    d[sx][sy] = 0
    
    # キューが空になるまでループ
    while que.qsize() > 0:
        # キューの先頭を取り出す
        p = que.get()
        # 取り出してきた状態がゴールなら探索をやめる
        if p[0] == gx and p[1] == gy:
            break
        # 移動4方向をループ
        for i in range(4):
            # 移動した後の点を(nx, ny)とする
            nx, ny = p[0] + dx[i], p[1] + dy[i]
            
            # 移動が可能かの判定とすでに訪れたことがあるかの判定
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] != "#" and d[nx][ny] == INF:
                que.put((nx, ny))
                d[nx][ny] = d[p[0]][p[1]] + 1
    return d[gx][gy]

def solve():
    res = bfs()
    print(res)


# input
N = int(input())
M = int(input())
for i in range(N):
    l = input()
    for j, c in enumerate(l):
        maze[i][j] = c
        if c == "S":
            sx, sy = i, j
        if c == "G":
            gx, gy = i, j

solve()

"""
sample input

10
10
#S######.#
......#..#
.#.##.##.#
.#........
##.##.####
....#....#
.#######.#
....#.....
.####.###.
....#...G#

sample output

22
"""

