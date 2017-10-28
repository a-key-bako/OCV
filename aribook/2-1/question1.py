# p.34 全探索 - 部分和問題
a = [0 for i in range(100000)]
n, k = 0, 0

def dfs(i, sum):
    if i == n:
        return sum == k
    if dfs(i + 1, sum):
        return True
    if dfs(i + 1, sum + a[i]):
        return True
    return False

def solve():
    if dfs(0, 0):
        print("Yes")
    else:
        print("No")

# input
n = int(input())
l = list(map(int, input().split()))
for i, a_i in enumerate(l):
    a[i] = a_i
k = int(input())

solve()

"""
sample input 1

4
1 2 4 7
13

sample output 1

Yes

sample input 2

4
1 2 4 7
15

sample output 2

No

"""
