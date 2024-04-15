"""
LeetCode [739]: Daily Temperatures

Given a list of daily temperatures, returns a list representing the number of days you would have to wait 
until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

Approach:
Iterate through the temperatures list and use a stack to keep track of indices of temperatures for which
we haven't found a warmer day yet. For each temperature, pop temperatures from the stack while the current
temperature is greater than the temperature at the index on top of the stack.

Code with Comments:
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []  # Initialize a stack to keep track of indices of temperatures
        n = len(temperatures)
        ans = [0] * n  # Initialize a list to store the results
        
        # Iterate through each temperature in the input list
        for idx in range(0, n): 
            # While there are temperatures in the stack and the current temperature is higher than the temperature
            # at the index on top of the stack
            while stack and temperatures[idx] > temperatures[stack[-1]]:
                # Pop temperatures from the stack and update the result list for the corresponding indices
                stack_idx = stack.pop()
                ans[stack_idx] = idx - stack_idx
                
            # Add the current index to the stack
            stack.append(idx)
        
        return ans
