"""
LeetCode [268]: Missing Number

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Approach:
1. Calculate the sum of the first n natural numbers using the formula n * (n + 1) // 2.
2. Calculate the sum of the elements in the given array nums.
3. The missing number is the difference between the sum of the first n natural numbers and the sum of the elements in nums.

Code with Comments:
"""

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Calculate the sum of the first n natural numbers
        n = len(nums)
        total = n * (n + 1) // 2
        # Calculate the sum of the elements in the given array nums
        nums_total = sum(nums)
        # Return the missing number
        return total - nums_total
