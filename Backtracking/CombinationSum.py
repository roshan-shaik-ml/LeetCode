"""
LeetCode [39]: Combination Sum

Given an array of distinct integers 'candidates' and a target integer 'target', return a list of all unique combinations of 'candidates' where the chosen numbers sum to 'target'. You may return the combinations in any order.

The same number may be chosen from 'candidates' an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to 'target' is less than 150 combinations for the given input.

Approach:
1. Sort the 'candidates' array to ensure the combinations are in ascending order.
2. Initialize an empty list 'result' to store the combinations.
3. Define a recursive function 'explore' to explore all possible combinations.
4. In the 'explore' function:
    - If 'target' becomes 0, append the current combination to 'result'.
    - Iterate through 'candidates' starting from the current index.
    - For each candidate, if subtracting it from 'target' is non-negative, recursively call 'explore' with the updated target and combination.
5. Return 'result' containing all unique combinations.

Code:
"""

class Solution:
    def __init__(self):
        self.result = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.explore(candidates, 0, target, [])          
        return self.result
    
    def explore(self, nums, idx, target, ans):
        if target == 0:
            self.result.append(ans[:])
            return
        
        for curr in range(idx, len(nums)):
            if curr < len(nums) and target - nums[curr] >= 0:
                ans.append(nums[curr])
                self.explore(nums, curr, target - nums[curr], ans)
                ans.pop()
            else:
                break
