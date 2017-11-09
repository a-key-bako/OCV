# 蟻本 p.49 貪欲法
def solve():
    N = int(input())
    L = list(map(int, input().split()))
    ans = 0
    # 板が1本になるまで適用
    while N > 1:
        # 一番短い板mil1、次に短い板mil2を求める
        mii1, mii2 = 0, 1
        if L[mii1] > L[mii2]:
            mii1, mii2 = mii2, mii1
        for i in range(2,N):
            if L[i] < L[mii1]:
                mii2 = mii1
                mii1 = i
            elif L[i] < L[mii2]:
                mii2 = i
        # それらを併合
        t = L[mii1] + L[mii2]
        ans += t
        
        if mii1 == N - 1:
            mii1, mii2 = mii2, mii1
        L[mii1] = t
        L[mii2] = L[N - 1]
        N -= 1
    print(ans)

solve()

"""
sample input 1
3
8 5 8

sample output 1
34
"""
