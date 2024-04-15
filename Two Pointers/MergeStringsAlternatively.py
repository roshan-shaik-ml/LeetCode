"""
LeetCode [1768]: Merge Strings Alternately

Given two strings word1 and word2, merge the strings alternatively, starting with word1. 
If one string is longer than the other, append the remaining characters of the longer string to the merged string.

Approach:
1. Iterate through the shorter length of the two words, appending characters alternately from both words.
2. Append the remaining characters of the longer word to the merged string.

Code with Comments:
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Merge two strings alternatively, starting with word1.

        Args:
        - word1: First input string
        - word2: Second input string

        Returns:
        - merged: Merged string with characters from both input strings alternatively
        """
        minimum = min(len(word1), len(word2))  # Find the length of the shorter word

        merged = ''  # Initialize an empty string to store the merged result
        for idx in range(0, minimum):
            # Append characters alternately from both words
            merged += word1[idx] + word2[idx]
        
        # If one word is longer than the other, append the remaining characters of the longer word
        if len(word1) < len(word2):
            merged += word2[len(word1):]
        elif len(word2) < len(word1):
            merged += word1[len(word2):]
        
        return merged
