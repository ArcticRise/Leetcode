"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

"""


def climbStairs(n: int) -> int:
    if n <= 3:
        return n
    
    dp = [0] * (n)
    dp[0] = 1
    dp[1] = 2
    for i in range(2,n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[-1]

Case1,Case2 = 2,4
print(climbStairs(Case1))
print(climbStairs(Case2))

"""

Time Complexity: O(N)
Space: O(N) because were using another array for memo

"""