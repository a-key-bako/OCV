# http://abc076.contest.atcoder.jp/tasks/abc076_c

def solve():
    S=input()
    T=input()
    i = -1
    for j in range(len(S)-len(T)+1):
        if all(a=="?" or a==b for a,b in zip(S[j:],T)):
            i = j
    if i == -1:
        print("UNRESTORABLE")
    else:
        ans = S[0:i] + T + S[i+len(T):]
        ans = ans.replace("?", "a")
        print(ans)
 
solve()
