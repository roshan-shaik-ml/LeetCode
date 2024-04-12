"""
LeetCode [15]: 3Sum

Given an integer array 'nums', return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. Notice that the solution set must not contain duplicate triplets.

Approach:
1. Sort the input array 'nums'.
2. Iterate through the array using a loop.
3. For each element at index 'i', initialize two pointers 'l' and 'r' to the next and last elements respectively.
4. While 'l' is less than 'r', calculate the sum of the triplet.
5. If the sum is less than 0, increment 'l'. If it's greater than 0, decrement 'r'.
6. If the sum is 0, add the triplet to the result.
7. To avoid duplicate triplets, increment 'l' and decrement 'r' until they are not pointing to the same element as before.
8. Return the list of unique triplets.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Initialize a list to store the result
        result = []
        # Sort the input array
        nums.sort()

        # Iterate through the array
        for i in range(0, len(nums)):
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Initialize two pointers
            l = i + 1
            r = len(nums) - 1

            # While left pointer is less than right pointer
            while l < r:
                # Calculate the sum of the triplet
                triplet = [nums[i], nums[l], nums[r]]
                total = sum(triplet)
                # If sum is less than 0, move left pointer to the right
                if total < 0:
                    l += 1
                # If sum is greater than 0, move right pointer to the left
                elif total > 0:
                    r -= 1
                # If sum is 0, add the triplet to result
                else:
                    result.append(triplet)
                    # Move left and right pointers until they're not pointing to the same element
                    while l < r and nums[l] == triplet[1]:
                        l += 1
                    while l < r and nums[r] == triplet[2]:
                        r -= 1
    
        # Return the result
        return result
