"""
LeetCode [50]: Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

Approach:
1. Implement a recursive function 'exponentiation' to perform the exponentiation.
2. If 'n' is 0, return 1.
3. If 'n' is even, recursively call 'exponentiation' with 'x' squared and 'n' divided by 2.
4. If 'n' is odd, recursively call 'exponentiation' with 'x' squared and ('n' - 1) divided by 2, and multiply the result by 'x'.
5. For negative 'n', compute the result for positive 'n' using 'exponentiation' and return the reciprocal if 'n' is negative.

Code:
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Implement a recursive function 'exponentiation' to perform the exponentiation
        result = self.exponentiation(x, abs(n))
        # For negative 'n', compute the result for positive 'n' and return the reciprocal
        if n > 0:
            return result
        return 1/result

    def exponentiation(self, x, n):
        # If 'n' is 0, return 1
        if n == 0:
            return 1
        # If 'n' is even, recursively call 'exponentiation' with 'x' squared and 'n' divided by 2
        if n % 2 == 0:
            return self.exponentiation(x * x, n//2)
        # If 'n' is odd, recursively call 'exponentiation' with 'x' squared and ('n' - 1) divided by 2, and multiply the result by 'x'
        else:
            return x * self.exponentiation(x * x, (n-1)//2)
