"""
LeetCode [46]: Permutations

Given a collection of distinct integers, return all possible permutations.

Approach:
1. Implement backtracking to generate all possible permutations.
2. Swap elements at different positions to generate permutations.
3. Recursively explore all possible choices until reaching the end of the array.
4. Backtrack by restoring the array to its original state after each exploration.

Code with Comments:
"""

from typing import List, Union

class Solution:

    def __init__(self):
        self.result = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Generates all possible permutations of the given list of numbers.

        Parameters:
        - nums: A list of distinct integers.

        Returns:
        - List[List[int]]: A list containing all possible permutations.
        """
        result = self.permutations(nums, 0)
        return result
    
    def permutations(self, nums: List[int], idx: int) -> Union[None, List[List[int]]]:
        """
        Recursively generates permutations using backtracking.

        Parameters:
        - nums: A list of distinct integers.
        - idx: The current index in the list.

        Returns:
        - Union[None, List[List[int]]]: None if the end of the list is reached, otherwise the list of permutations.
        """
        if idx == len(nums):
            # Base case: When the current index reaches the end of the list, add the permutation to the result.
            self.result.append(nums[:])
            return None
        
        for i in range(idx, len(nums)):
            # Iterate through the remaining elements to generate permutations.
            # Swap the current element with each element from idx to the end, then recursively generate permutations.
            nums[i], nums[idx] = nums[idx], nums[i]
            self.permutations(nums, idx + 1)
            nums[i], nums[idx] = nums[idx], nums[i]

        return self.result
