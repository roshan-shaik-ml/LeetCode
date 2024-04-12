"""
Approach:
1. Define constants for the maximum and minimum integer values allowed.
2. Initialize variables to store the result, flag for negative numbers, and handle the input if it's negative.
3. Iterate through the input number, extracting digits and reversing the number.
4. Check for overflow by comparing the result with the defined constants.
5. Return the reversed number with appropriate sign.
"""

class Solution:
    def reverse(self, x: int) -> int:
        # Define constants for the maximum and minimum integer values allowed
        const1 = math.pow(2, 31) - 1
        const2 = -math.pow(2, 31)

        # Initialize variables
        ans = 0
        isNegative = False
        
        # Handle negative input
        if x < 0:
            x = abs(x)
            isNegative = True

        # Iterate through the input number and reverse it
        while x != 0:
            # Check for overflow
            if ans > const1 // 10 or ans < const2 // 10:
                return 0

            digit = x % 10
            ans =  ans * 10 + digit
            x = x // 10

        # Return the reversed number with appropriate sign
        if isNegative:
            return 0 - ans
        return ans
