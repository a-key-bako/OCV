# 蟻本 p.30 再帰関数
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
