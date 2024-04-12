"""
LeetCode [16]: 3Sum Closest

Given an integer array 'nums' of length 'n' and an integer 'target', find three integers in 'nums' such that the sum is closest to 'target'. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Approach:
1. Sort the input array 'nums'.
2. Initialize variables to store the closest sum found so far ('ans') and the difference between the sum and the target ('difference').
3. Iterate through the array using a loop.
4. For each element at index 'i', initialize two pointers 'left' and 'right' to the next and last elements respectively.
5. While 'left' is less than 'right', calculate the sum of the triplet.
6. Update 'difference' if the absolute difference between the current sum and 'target' is smaller than the previous difference.
7. Update 'ans' to the current sum if the absolute difference is updated.
8. If the current sum equals 'target', return 'target' as it is the closest sum possible.
9. If the current sum is less than 'target', move 'left' pointer to the right. Otherwise, move 'right' pointer to the left.
10. Return 'ans' as the closest sum found.
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sort the input array
        nums.sort()
        # Initialize variables for the closest sum and the difference between the sum and target
        ans = sum(nums[:3])
        difference = float('inf')

        # Iterate through the array
        for i in range(0, len(nums)-2):
            # Initialize two pointers
            left = i + 1
            right = len(nums) - 1

            # While left pointer is less than right pointer
            while left < right:
                # Calculate the sum of the triplet
                triplet = [nums[i], nums[left], nums[right]]
                total = sum(triplet)

                # Update difference and ans if needed
                if abs(target - total) < abs(difference):
                    difference = abs(target - total)
                    ans = total

                # If current sum equals target, return target
                if total == target:
                    return target
                # If current sum is less than target, move left pointer to the right
                elif total < target:
                    left += 1
                # If current sum is greater than target, move right pointer to the left
                else:
                    right -= 1
        
        # Return the closest sum found
        return ans
