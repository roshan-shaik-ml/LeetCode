"""
LeetCode [338]: Counting Bits

Given a non-negative integer num, for every number i in the range 0 ≤ i ≤ num, calculate the number of 1's in their binary representation and return them as an array.

Approach:
1. Create a helper function getOnes(num) that counts the number of set bits (1's) in the binary representation of a number.
2. Iterate through the range from 0 to n inclusive and for each number i, calculate the number of 1's using the helper function and append it to the result array.

Code with Comments:
"""

from typing import List

class Solution:

    # Helper function to count the number of set bits in a number
    def getOnes(self, num):
        count = 0
        while num != 0:
            count += 1
            num = num & (num - 1)
        return count

    # Main function to count bits for numbers from 0 to n
    def countBits(self, n: int) -> List[int]:
        ans = []
        # Iterate through the range from 0 to n
        for i in range(n + 1):
            # Calculate the number of set bits for each number and append to the result array
            ans.append(self.getOnes(i))
        return ans
