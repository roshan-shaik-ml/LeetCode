"""
LeetCode [217]: Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Approach:
Use a set to store the unique elements encountered while iterating through the array. If a duplicate element is found, return True; otherwise, return False.

Code with Comments:
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Initialize a set to store unique elements
        freq = set()
        # Iterate through the array
        for num in nums:
            # Check if the current number is already in the set
            if num in freq:
                # If the number is already in the set, it is a duplicate
                return True
            else:
                # If the number is not in the set, add it to the set
                freq.add(num)
        # No duplicates found in the array
        return False
