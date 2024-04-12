"""
LeetCode [49]: Group Anagrams

Given an array of strings 'strs', group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Approach:
1. Create a dictionary 'mp' to store the sorted string as key and list of anagrams as value.
2. Iterate through each string in 'strs'.
3. Sort each string and join them to get a sorted string representation.
4. If the sorted string is not in the dictionary, add it with the string as value.
5. If it already exists, append the string to the list of anagrams.
6. Iterate through the keys of the dictionary and append the lists of anagrams to the answer list.
7. Return the answer list.

Code:
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary to store the sorted string as key and list of anagrams as value
        mp = {}
        for string in strs:
            # Sort each string and join them to get a sorted string representation
            sorted_str = ''.join(sorted(string))
            if mp.get(sorted_str) is None:
                mp[sorted_str] = [string]
            else:
                mp[sorted_str].append(string)
        
        # Iterate through the keys of the dictionary and append the lists of anagrams to the answer list
        ans = []
        for key in mp.keys():
            ans.append(mp[key])
        
        # Return the answer list
        return ans
