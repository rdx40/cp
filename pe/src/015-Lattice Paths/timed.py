import time
import math

# Combinatorics method
start = time.time()
result = math.comb(40, 20)
end = time.time()
print("Combinatorics result:", result)
print("Time taken:", end - start, "seconds")

# Dynamic Programming method
def lattice_paths_dp(n):
    dp = [[0] * (n+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[n][n]

start = time.time()
result = lattice_paths_dp(20)
end = time.time()
print("DP result:", result)
print("Time taken:", end - start, "seconds")

