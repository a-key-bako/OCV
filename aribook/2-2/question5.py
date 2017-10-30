# 蟻本 p.43 貪欲法
MAX_N = 100000

def solve():
    # 仕事をソートするための配列
    itv = []
    # pairはサイズ2のtapleで代用
    for i in range(N):
        itv.append((T[i], S[i]))
    itv.sort()
    # tは最後に選んだ仕事の終了時間
    ans, t = 0, 0
    for i in range(N):
        if t < itv[i][1]:
            ans += 1
            t = itv[i][0]
    print(ans)

# input
N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

solve()

"""
sample input
5
1 2 4 6 8
3 5 7 9 10

sample output
3
"""
