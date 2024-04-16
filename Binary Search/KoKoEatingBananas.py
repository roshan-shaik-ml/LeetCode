"""
LeetCode [875]: Koko Eating Bananas

Koko loves to eat bananas. There are `n` piles of bananas, the `i-th` pile has `piles[i]` bananas. 
The guards have gone and will come back in `h` hours.

Koko can decide her eating speed of `k` bananas per hour. Each hour, she chooses some pile of bananas and 
eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and 
will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer `k` such that she can eat all the bananas within `h` hours.

Example:
Input: piles = [3,6,7,11], h = 8
Output: 4
Explanation: Koko can eat bananas with speeds: 1, 2, 3, 4, 5, or 6.
The minimum speed to eat all bananas within 8 hours is 4.

Approach:
We need to find the minimum eating speed `k` that allows Koko to eat all bananas within `h` hours. 
This problem can be solved using binary search. We can perform a binary search for the minimum 
eating speed within the range of 1 to the maximum number of bananas in a pile. 
For each mid speed, we check if it is possible to eat all bananas within `h` hours. 
If possible, we update the result to the current mid speed and adjust the search range accordingly. 
If not possible, we adjust the search range accordingly and continue the binary search.

Code with Comments:
"""

import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Finds the minimum eating speed required for Koko to eat all bananas within `h` hours.

        Args:
        piles: A list of integers representing the number of bananas in each pile.
        h: An integer representing the number of hours Koko has before the guards return.

        Returns:
        The minimum integer eating speed `k` such that Koko can eat all bananas within `h` hours.
        """
        # Sort the piles to have a clear understanding of the range of eating speeds
        piles.sort()
        # Define the search range for eating speeds
        least, most = 1, max(piles)
        # Initialize the result to infinity
        result = float('inf')

        # Binary search for the minimum eating speed
        while least <= most:
            # Calculate the mid eating speed
            mid = (least + most) >> 1

            # Check if it is possible to eat all bananas within h hours with the current mid speed
            if self.isPossibleToEat(piles, mid, h):
                # If it is possible to eat all bananas within the given hours with the current mid speed,
                # update the result to the current mid speed because we are looking for the minimum eating speed
                result = min(result, mid)
                # Since we are looking for the minimum eating speed, we adjust the search range to the left
                # by setting the upper bound (most) to mid - 1
                most = mid - 1
            else:
                # If it is not possible to eat all bananas within the given hours with the current mid speed,
                # we need to increase the eating speed. So, we adjust the search range to the right
                # by setting the lower bound (least) to mid + 1
                least = mid + 1

        # Return the minimum eating speed required
        return result
        
    def isPossibleToEat(self, piles: List[int], mid: int, hours: int) -> bool:
        """
        Checks if it is possible to eat all bananas within the given hours with a certain eating speed.

        Args:
        piles: A list of integers representing the number of bananas in each pile.
        mid: An integer representing the current eating speed.
        hours: An integer representing the number of hours Koko has before the guards return.

        Returns:
        True if it is possible to eat all bananas within the given hours with the current eating speed, False otherwise.
        """
        # Initialize the total time required to eat all bananas
        totalTime = 0
        # Iterate through each pile of bananas
        for pile in piles:
            # Calculate the time required to eat the current pile with the current eating speed
            # and add it to the total time
            totalTime += math.ceil(pile / mid)
        
        # Check if the total time required is less than or equal to the given hours
        return totalTime <= hours
