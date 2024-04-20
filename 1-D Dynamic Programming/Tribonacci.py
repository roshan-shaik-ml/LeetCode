"""
The Tribonacci sequence Tn is defined as follows:
- T0 = 0, T1 = 1, T2 = 1, and Tn = Tn-1 + Tn-2 + Tn-3 for n >= 3.
- Given n, return the value of Tn.

Approach:
- We can solve this problem using dynamic programming with memoization.
- We initialize a list `memo` to store the Tribonacci numbers up to index 37.
- We set memo[0] = 0, memo[1] = 0, and memo[2] = 1 as per the sequence definition.
- For any index `n` greater than 2, we recursively calculate memo[n] using the memoization technique.
- If memo[n] is already calculated, we return it. Otherwise, we calculate it by summing the values of memo[n-3], memo[n-2], and memo[n-1].
- Finally, we return memo[n].

Complexity Analysis:
- The time complexity of this approach is O(n), where n is the input value.
- The space complexity is O(n) since we use memoization to store the Tribonacci numbers.
"""
class Solution:

    def __init__(self):
        # Initialize memoization list with values for indices 0, 1, and 2
        self.memo = [0] * 38
        self.memo[0] = 0
        self.memo[1] = 0
        self.memo[2] = 1

    def tribonacci(self, n: int) -> int:
        # Base cases
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        # Check if the value is already memoized
        if self.memo[n] != 0:
            return self.memo[n]
        else:
            # Recursively calculate and memoize the Tribonacci number for index n
            self.memo[n] = self.tribonacci(n - 3) + self.tribonacci(n - 2) + self.tribonacci(n - 1)
        
        # Return the calculated value
        return self.memo[n]
