"""
LeetCode [567]: Permutation in String

Given two strings s1 and s2, return true if s2 contains the permutation of s1.

Approach:
- Use two hash tables to store the frequency of characters in both strings.
- Slide a window of length equal to the length of s1 over s2.
- Check if the hash tables for both strings match at each window position.
- If a match is found, return True. Otherwise, continue sliding the window until the end of s2 is reached.

"""

from collections import defaultdict

class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Get the lengths of both strings
        n1 = len(s1)
        n2 = len(s2)

        # If the length of s1 is greater than s2, return False
        if n1 > n2:
            return False

        # Initialize two hash tables to store the frequency of characters in s1 and the sliding window of s2
        hashtable1 = defaultdict(int)
        hashtable2 = defaultdict(int)

        # Fill the hash table for s1 with the frequency of characters
        for i in range(n1):
            hashtable1[s1[i]] += 1
            hashtable2[s2[i]] += 1

        # Slide the window over s2 and compare hash tables
        for idx in range(n1, n2):
            # If the hash tables match, return True
            if hashtable2 == hashtable1:
                return True

            # Add the next letter to the current window
            hashtable2[s2[idx]] += 1

            # Remove the first character of the previous window
            if hashtable2[s2[idx - n1]] == 1:
                del hashtable2[s2[idx - n1]]
            else:
                hashtable2[s2[idx - n1]] -= 1
        
        # Check if the hash tables match at the end of s2
        return (hashtable1 == hashtable2)
