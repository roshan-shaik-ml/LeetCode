"""
LeetCode [2380]: Time Needed to Rearrange a Binary String

Given a binary string `s`, you need to find the minimum number of seconds to remove all occurrences of the substring '01' by replacing it with '10'.

Approach:
Iterate through the string and count the occurrences of '01'. Replace each occurrence of '01' with '10' until no occurrences of '01' are left.

Code with Comments:
"""

class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        """
        Calculate the minimum number of seconds to remove all occurrences of '01' in the string.

        Args:
        - s: Binary string where occurrences of '01' need to be removed

        Returns:
        - count: Minimum number of seconds to remove all occurrences of '01'
        """
        count = 0  # Initialize the count of seconds to 0
        
        # Continue the loop until no occurrences of '01' are left in the string
        while s.count('01') != 0:
            s = s.replace('01', '10')  # Replace each occurrence of '01' with '10'
            count += 1  # Increment the count of seconds
        
        return count  # Return the minimum number of seconds
