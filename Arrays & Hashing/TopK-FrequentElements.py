"""
LeetCode [347]: Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Approach:
1. Count the frequency of each element in the array using a Counter.
2. Sort the elements based on their frequency in descending order.
3. Return the first k elements from the sorted list.

Code with Comments:
"""

from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each element
        freq = Counter(nums)
        # Sort elements based on frequency in descending order
        freq = dict(sorted(freq.items(), key=lambda kv: kv[1], reverse=True))
        # Extract keys (elements) from the dictionary and return the first k elements
        ans = list(freq.keys())
        return ans[:k]
