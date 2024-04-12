"""
LeetCode [11]: Container With Most Water

Given 'n' non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 'n' vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Approach:
1. Initialize two pointers, 'ptr1' and 'ptr2', at the beginning and end of the array respectively.
2. Iterate while 'ptr1' is less than 'ptr2'.
3. Calculate the area between the two pointers by multiplying the minimum height of the two pointers by the distance between them.
4. Update the maximum area found so far.
5. Move the pointer with the smaller height towards the other pointer.
6. Return the maximum area found.
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize two pointers at the beginning and end of the array
        ptr1 = 0
        ptr2 = len(height) - 1

        # Initialize variable to store the maximum area found
        ans = 0

        # Iterate while the two pointers don't cross each other
        while ptr1 < ptr2:
            # Calculate the area between the two pointers
            curr = min(height[ptr1], height[ptr2]) * (ptr2 - ptr1)
            # Update the maximum area found so far
            ans = max(curr, ans)
            # Move the pointer with the smaller height towards the other pointer
            if height[ptr1] <= height[ptr2]:
                ptr1 += 1
            else:
                ptr2 -= 1
        
        # Return the maximum area found
        return ans
