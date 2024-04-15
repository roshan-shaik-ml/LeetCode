"""
LeetCode [238]: Product of Array Except Self

Given an array nums of n integers where n > 1, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Approach:
1. Initialize two arrays, prefix and suffix, both of length n, where prefix[i] stores the product of all elements to the left of nums[i] (excluding nums[i]), and suffix[i] stores the product of all elements to the right of nums[i] (excluding nums[i]).
2. Iterate over the input array nums to populate the prefix array, starting with prefix[0] = 1 and then multiplying each element with the previous prefix value.
3. Iterate over the input array nums in reverse order to populate the suffix array, starting with suffix[n-1] = 1 and then multiplying each element with the previous suffix value.
4. Initialize an answer array ans of length n, where ans[i] = prefix[i] * suffix[i], representing the product of all elements except nums[i].

Code with Comments:
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Initialize prefix and suffix arrays
        prefix = [1] * n
        suffix = [1] * n
        ans = [1] * n
        
        # Calculate prefix products
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        # Calculate suffix products
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        # Calculate product except self
        for i in range(n):
            ans[i] = prefix[i] * suffix[i]
        
        return ans
