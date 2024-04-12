"""
LeetCode [55]: Jump Game

Given an array of non-negative integers 'nums', you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you can reach the last index.

Approach:
1. Initialize 'idx' to 0 to represent the current position and 'jumps' to nums[0] to represent the maximum jump from the current position.
2. Iterate through the array while there are still jumps available and the index is within bounds.
3. Decrement 'jumps' by 1 and update it with the maximum of its current value and the jump value at the next index.
4. Move to the next index.
5. If the loop completes and 'idx' reaches the last index of the array, return True, indicating that the last index is reachable. Otherwise, return False.

Code:
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Initialize 'idx' and 'jumps'
        idx = 0
        jumps = nums[idx]

        # Iterate through the array while there are still jumps available and the index is within bounds
        while jumps != 0 and idx < len(nums):
            # Decrement 'jumps' by 1 and update it with the maximum of its current value and the jump value at the next index
            jumps -= 1
            jumps = max(jumps, nums[idx])
            # Move to the next index
            idx += 1

        # Check if 'idx' reaches the last index of the array and return True or False accordingly
        return idx == len(nums)
