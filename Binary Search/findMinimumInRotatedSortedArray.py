"""
LeetCode [153]: Find Minimum in Rotated Sorted Array

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
Given the rotated sorted array nums, return the minimum element of this array.

Approach:
1. Use binary search to efficiently find the minimum element in the rotated sorted array.
2. Initialize pointers low and high to perform binary search.
3. While searching, update the minimum element if necessary based on the current mid value.

Code with Comments:
"""

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initialize variables
        low = 0
        high = len(nums) - 1
        mini = nums[low]  # Initialize mini with the first element
        
        # Perform binary search to find the minimum element
        while low <= high:
            # Check if the array is sorted (no rotation)
            if nums[low] < nums[high]:
                mini = min(mini, nums[low])  # Update mini if necessary
                break  # Exit the loop as the array is sorted
            
            mid = (low + high) // 2  # Calculate the midpoint
            
            # Update mini with the minimum value among mini and the element at mid
            mini = min(mini, nums[mid])
            
            # Determine which half to search next
            if nums[mid] >= nums[low]:
                low = mid + 1
            else:
                high = mid - 1
        
        return mini  # Return the minimum element
