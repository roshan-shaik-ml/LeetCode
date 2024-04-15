"""
LeetCode [125]: Valid Palindrome

Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Approach:
1. Convert the string to lowercase to ignore case sensitivity.
2. Iterate through the string and construct a new string containing only alphanumeric characters.
3. Use two pointers to check if the new string is a palindrome.
4. Compare characters from the beginning and end of the string until the pointers meet.
5. If all characters match, return True; otherwise, return False.

Code with Comments:
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert the string to lowercase
        s = s.lower()
        
        # Construct a new string with only alphanumeric characters
        string = ''
        for char in s:
            if char.isalnum():
                string += char
        
        # Check if the new string is empty (i.e., contains no alphanumeric characters)
        if len(string) == 0:
            return True

        # Initialize pointers for comparing characters
        ptr1 = 0
        ptr2 = len(string) - 1

        # Use two pointers to check if the string is a palindrome
        while ptr1 < ptr2:
            # Compare characters from the beginning and end of the string
            if string[ptr1] == string[ptr2]:
                ptr1 += 1
                ptr2 -= 1
            else:
                return False

        # If all characters match, return True
        return True
