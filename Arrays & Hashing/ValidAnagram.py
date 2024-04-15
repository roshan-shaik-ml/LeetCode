"""
LeetCode [242]: Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Approach:
1. Use Python's Counter class to count the occurrences of characters in both strings.
2. Check if the Counter objects for both strings are equal. If they are equal, return True; otherwise, return False.

Code with Comments:
"""

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if the Counter objects for both strings are equal
        return Counter(s) == Counter(t)
