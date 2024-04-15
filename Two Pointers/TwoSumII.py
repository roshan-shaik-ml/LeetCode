"""
LeetCode [167]: Two Sum II - Input array is sorted

Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.

Approach:
1. Use two pointers approach with one pointer starting from the beginning and another starting from the end of the array.
2. Iterate through the array until the two pointers meet.
3. At each iteration, calculate the sum of the numbers at the two pointers.
4. If the sum is equal to the target, return the indices of the two numbers.
5. If the sum is greater than the target, decrement the pointer at the end.
6. If the sum is less than the target, increment the pointer at the beginning.

Code with Comments:
"""

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers
        ptr1, ptr2 = 0, len(numbers) - 1

        # Iterate until the two pointers meet
        while ptr1 < ptr2:
            # Calculate the sum of the numbers at the two pointers
            curr_sum = numbers[ptr1] + numbers[ptr2]
            # If the sum is equal to the target, return the indices
            if curr_sum == target:
                return [ptr1 + 1, ptr2 + 1]
            # If the sum is greater than the target, decrement ptr2
            elif curr_sum > target:
                ptr2 -= 1
            # If the sum is less than the target, increment ptr1
            else:
                ptr1 += 1
