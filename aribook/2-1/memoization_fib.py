# 蟻本 p.30 再帰関数
memo = [0 for i in range(100000)]

def fib(n):
    if n <= 1:
        return n
    if memo[n] != 0:
        return memo[n]
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]
