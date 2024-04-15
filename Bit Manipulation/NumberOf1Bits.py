"""
LeetCode [191]: Number of 1 Bits

Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Approach:
Iterate through each bit of the integer and count the number of '1' bits using the bitwise AND operation with (n-1).

Code with Comments:
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        # Initialize a variable to count the number of '1' bits
        count = 0
        # Iterate until n becomes 0
        while n != 0:
            # Increment the count for each '1' bit encountered
            count += 1
            # Unset the rightmost '1' bit by performing bitwise AND with (n-1)
            n = n & (n - 1)
        # Return the total count of '1' bits
        return count
