# 蟻本 p.42 貪欲法

# コインの金額
V = (1, 5, 10, 50, 100, 500)
A = 0

def solve():
    ans = 0
    a = A
    for i in reversed(range(6)):
        t = min(a//V[i], C[i])
        a -= t * V[i]
        ans += t
    print(ans)

# input
C = list(map(int, input().split()))
A = int(input())

solve()

"""
sample input

3 2 1 3 0 2
620

sample output

6
"""
