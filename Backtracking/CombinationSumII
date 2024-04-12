"""
LeetCode [40]: Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Approach:
1. Sort the 'candidates' array to ensure the combinations are in ascending order.
2. Initialize an empty list 'result' to store the combinations.
3. Define a recursive function 'explore' to explore all possible combinations.
4. In the 'explore' function:
    - If 'target' becomes 0, append the current combination to 'result'.
    - Iterate through 'candidates' starting from the current index.
    - For each candidate, if subtracting it from 'target' is non-negative, recursively call 'explore' with the updated target and combination.
    - Maintain a 'prev_element' variable to avoid duplicate combinations.
5. Return 'result' containing all unique combinations.

Code:
"""

class Solution:
    def __init__(self):
        self.result = []
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.explore(candidates, 0, target, [])          
        return self.result
    
    def explore(self, nums, idx, target, ans):
        if target == 0:
            self.result.append(ans[:])
            return
        
        prev_element = -1
        for curr in range(idx, len(nums)):
            # Make sure the previous popped element != current element
            # This helps to avoid duplicates.
            if nums[curr] == prev_element:
                continue
            elif curr < len(nums) and target - nums[curr] >= 0:
                ans.append(nums[curr])
                self.explore(nums, curr + 1, target - nums[curr], ans)
                prev_element = ans.pop()
