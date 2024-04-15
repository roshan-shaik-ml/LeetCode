"""
LeetCode [128]: Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

Approach:
1. Convert the given list of numbers into a set to efficiently check for presence.
2. Initialize the answer variable 'ans' to store the length of the longest consecutive sequence.
3. Iterate through each number in the list.
4. For each number, check if its predecessor (num - 1) exists in the set.
5. If it does, continue to the next number since it cannot be the starting point of a sequence.
6. If it doesn't, initialize a variable 'curr' to the current number and a variable 'length' to 0.
7. While 'curr' exists in the set, increment 'curr' by 1 and increment 'length' by 1.
8. Update 'ans' to be the maximum of 'length' and 'ans'.
9. Return 'ans' as the length of the longest consecutive sequence.

Code with Comments:
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert the list of numbers into a set for efficient presence check
        numberSet = set(nums)

        # Initialize the answer variable to store the length of the longest consecutive sequence
        ans = 0

        # Iterate through each number in the list
        for num in nums:
            # Check if the predecessor of the current number exists in the set
            if (num - 1) in numberSet:
                # If it exists, continue to the next number
                continue
            else:
                # If it doesn't exist, initialize variables for tracking the consecutive sequence
                curr = num
                length = 0
                # While 'curr' exists in the set, increment 'curr' and 'length'
                while curr in numberSet:
                    curr += 1
                    length += 1
                # Update 'ans' to be the maximum of 'length' and the current 'ans'
                ans = max(length, ans)
        
        # Return the final answer, which is the length of the longest consecutive sequence
        return ans
