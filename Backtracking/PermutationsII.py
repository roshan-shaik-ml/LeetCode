"""
LeetCode [47]: Permutations II

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Approach:
1. Implement backtracking to generate all possible permutations.
2. Use a set to keep track of visited elements to avoid duplicate permutations.
3. Sort the input list to handle duplicates efficiently.
4. Recursively explore all possible choices until reaching the end of the array.
5. Backtrack by restoring the array to its original state after each exploration.

Code with Comments:
"""

from typing import List

class Solution:

    def __init__(self):
        self.result = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        Generates all possible unique permutations of the given list of integers.

        Parameters:
        - nums: A list of integers (may contain duplicates).

        Returns:
        - List[List[int]]: A list containing all possible unique permutations.
        """
        nums.sort()  # Sort the input list to handle duplicates efficiently.
        result = self.permutations(nums, 0)
        return result
    
    def permutations(self, nums: List[int], idx: int) -> List[List[int]]:
        """
        Recursively generates unique permutations using backtracking.

        Parameters:
        - nums: A list of integers.
        - idx: The current index during the permutation generation process.

        Returns:
        - List[List[int]]: A list containing all possible unique permutations.
        """
        if idx == len(nums):
            # Base case: When the current permutation size equals the input list size, add it to the result.
            self.result.append(nums[:])
            return
        
        seen = set()  # Keep track of visited elements to avoid duplicate permutations.
        for i in range(idx, len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                nums[i], nums[idx] = nums[idx], nums[i]  # Swap elements to explore different permutations.
                self.permutations(nums, idx+1)  # Recursively generate permutations.
                nums[i], nums[idx] = nums[idx], nums[i]  # Backtrack: Restore the array to its original state.
        
        return self.result
