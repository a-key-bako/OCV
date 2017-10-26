# 蟻本 p.30 再帰関数
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)
