"""
Approach:
1. Initialize two pointers, 'low' and 'high', to the start and end of the array respectively.
2. Use a while loop to iterate until 'low' is less than or equal to 'high'.
3. Inside the loop, calculate the mid index.
4. Check if the element at the mid index is equal to the target. If it is, return the mid index.
5. Check if the left half of the array (from 'low' to 'mid') is sorted.
    - If the left half is sorted and the target is within the range of the left half, update 'high' to mid - 1.
    - Otherwise, update 'low' to mid + 1.
6. If the left half is not sorted, check if the right half of the array (from 'mid' to 'high') is sorted.
    - If the right half is sorted and the target is within the range of the right half, update 'low' to mid + 1.
    - Otherwise, update 'high' to mid - 1.
7. If the target is not found in the array, return -1.

Code:
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize 'low' and 'high' pointers
        low = 0
        high = len(nums) - 1

        # Binary search loop
        while(low <= high):
            # Calculate mid index
            mid = (high + low) // 2

            # Check if target is found at mid index
            if(nums[mid] == target):
                return mid

            # Check if left half of array (from 'low' to 'mid') is sorted
            if(nums[low] <= nums[mid]):
                # If left half is sorted and target is within the range, update 'high'
                if (nums[low] <= target < nums[mid]):
                    high = mid - 1
                else:
                    low = mid + 1   
            # Check if right half of array (from 'mid' to 'high') is sorted
            else:
                # If right half is sorted and target is within the range, update 'low'
                if (nums[mid] < target <= nums[high]):
                    low = mid + 1
                else:
                    high = mid - 1

        # If target is not found, return -1
        return -1
