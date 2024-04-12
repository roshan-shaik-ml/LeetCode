"""
LeetCode [34]: Find First and Last Position of Element in Sorted Array

Given an array of integers 'nums' sorted in ascending order, find the starting and ending position of a given 'target' value. 
If 'target' is not found in the array, return '[-1, -1]'.

You must write an algorithm with O(log n) runtime complexity.

Approach:
1. Initialize 'low' and 'high' pointers to -1, indicating the initial range of the target.
2. Perform a binary search to find the index of the target in the array.
3. If the target is not found, return [-1, -1].
4. If the target is found at index 'idx', set 'low' and 'high' to 'idx'.
5. Extend the range of 'low' to the left until the previous element is not equal to the target.
6. Extend the range of 'high' to the right until the next element is not equal to the target.
7. Return [low, high], representing the range of occurrences of the target.

Code:
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Initialize 'low' and 'high' pointers
        low, high = -1, -1

        # Perform binary search to find the index of the target
        idx = self.binarySearch(nums, target)
        
        # If target is not found, return [-1, -1]
        if idx == -1:
            return [low, high]

        # If target is found, set 'low' and 'high' to 'idx'
        low, high = idx, idx
        size = len(nums)
        
        # Extend the range of 'low' to the left
        while low - 1 >= 0:
            if nums[low - 1] == target:
                low -= 1
            else:
                break
        
        # Extend the range of 'high' to the right
        while high + 1 < size:
            if nums[high + 1] == target:
                high += 1
            else:
                break
            
        # Return [low, high], representing the range of occurrences of the target
        return [low, high]
    
    # Binary search implementation
    def binarySearch(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1
