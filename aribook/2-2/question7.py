# 蟻本 p.47 貪欲法
def solve():
    # input
    N = int(input())
    R = int(input())
    X = list(map(int, input().split()))

    X.sort()
    i, ans = 0, 0
    while i < N:
        # sはカバーされていない一番左の点の位置
        s = X[i]
        i += 1
        # sから距離Rを超える点まで進む
        while i < N and X[i] <= s + R:
            i += 1
        # pは新しく印を付ける点の位置
        p = X[i-1]
        # pから距離Rを超える点まで進む
        while i < N and X[i] <= p + R:
            i += 1
        ans +=1
    
    print(ans)

solve()


"""
sample input
6
10
1 7 15 20 30 50

sample output
3
"""
