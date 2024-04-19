class Solution:
    """
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. 
    In how many distinct ways can you climb to the top?

    Approach:
    - We can solve this problem using dynamic programming.
    - We initialize a list `dp` to store the number of distinct ways to reach each step.
    - Since there is only 1 way to reach the 0th and 1st steps, we initialize `dp` with [1, 1].
    - For each step `i` from 2 to `n`, we calculate the number of distinct ways to reach that step
      by summing up the number of ways to reach the previous two steps (`i-1` and `i-2`).
    - Finally, we return `dp[n]`, which represents the number of distinct ways to reach the `n`th step.

    Complexity Analysis:
    - The time complexity of this approach is O(n), where n is the total number of steps.
    - The space complexity is also O(n) since we use a list of size n to store the dynamic programming values.
    """

    def climbStairs(self, n: int) -> int:
        dp = [1, 1]
        for i in range(2, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[n]
