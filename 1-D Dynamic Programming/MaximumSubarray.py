"""
LeetCode [53]: Maximum Subarray

Given an integer array 'nums', find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Approach:
1. Initialize 'current' and 'max_sum' to track the current sum and maximum sum.
2. Iterate through the 'nums' array.
3. Update 'current' by taking the maximum of 'current' and 0, to reset the sum if it becomes negative.
4. Add the current number to 'current'.
5. Update 'max_sum' to the maximum of 'current' and 'max_sum'.
6. Return 'max_sum'.

Code:
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize 'current' and 'max_sum'
        current = 0
        max_sum = float("-infinity")

        # Iterate through the 'nums' array
        for i in range(0, len(nums)):
            # Update 'current' by taking the maximum of 'current' and 0
            current = max(current, 0)
            # Add the current number to 'current'
            current += nums[i]
            # Update 'max_sum' to the maximum of 'current' and 'max_sum'
            max_sum = max(current, max_sum)

        # Return 'max_sum'
        return max_sum
