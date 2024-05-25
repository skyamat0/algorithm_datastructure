import sys
from typing import List

def dp_frog(N: int, H: List[int]) -> int:
    INF = 10**5
    dp = [INF for _ in range(N)]
    dp[0] = H[0]
    queue = [0]
    res = INF
    for i in range(N-1):
        while queue:
            tmp = queue.pop(0)
            if tmp + 1 < N:
                queue.append(tmp+1)
                if dp[tmp] + abs(H[tmp] - H[tmp+1]) < dp[tmp+1]:
                    dp[tmp+1] = dp[tmp] + abs(H[tmp] - H[tmp+1]) 
            if tmp + 2 < N:
                queue.append(tmp+2)
                if dp[tmp] + abs(H[tmp] - H[tmp+2]) < dp[tmp+2]:
                    dp[tmp+2] = dp[tmp] + abs(H[tmp] - H[tmp+2]) 
    print(dp[N-1]-10)
    return 0

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    H = list(map(int, sys.stdin.readline().split()))
    dp_frog(N, H)