# 蟻本 p.45 貪欲法
def solve():
    # S[a], a[a+1], S[b]が残っている文字列
    ans = ""
    a, b = 0, N-1
    
    while a <= b:
        # 左から見た場合と右から見た場合を比較
        left = False
        for i in range(b-a):
            if S[a+i] < S[b-i]:
                left = True
                break
            elif S[a+i] > S[b-i]:
                left = False
                break
        if left:
            ans += S[a]
            a += 1
        else:
            ans += S[b]
            b -= 1
    print(ans)

# input
N = int(input())
S = input()

solve()

"""
sample input
6
ACBBCB

sample output
ABCBCD

"""
