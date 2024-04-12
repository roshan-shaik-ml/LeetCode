"""
LeetCode [28]: 

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Approach:
1. Check if the haystack is equal to the needle. If it is, return 0.
2. Iterate through the haystack using a loop.
3. For each index 'i' from 0 to len(haystack) - len(needle), check if the substring of haystack starting at index 'i' and having the same length as needle matches the needle.
4. If a match is found, return the index 'i'.
5. If no match is found, return -1.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Check if haystack is equal to needle. If it is, return 0
        if haystack == needle:
            return 0

        # Iterate through the haystack using a loop
        for i in range(0, len(haystack) - len(needle) + 1):
            # Check if the substring of haystack matches the needle
            if haystack[i:i+len(needle)] == needle:
                return i

        # If no match is found, return -1
        return -1
