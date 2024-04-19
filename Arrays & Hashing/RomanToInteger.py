"""
LeetCode [13]: Roman to Integer

Given a roman numeral, convert it to an integer.

Approach:
- Create a hash map to store the integer values corresponding to each roman numeral character.
- Iterate through the input string.
- If the value of the current roman numeral character is less than the value of the next character, subtract its value from the total.
- Otherwise, add its value to the total.
- Return the total.

"""

class Solution:

    def romanToInt(self, s: str) -> int:
        
        # Create a hash map to store the integer values of each roman numeral character
        hashmap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        # Initialize the total sum
        total = 0
        
        # Iterate through the string
        for idx in range(len(s) - 1):
            # If the value of the current character is less than the next character, subtract its value
            if hashmap[s[idx]] < hashmap[s[idx + 1]]:
                total -= hashmap[s[idx]]
            else:
                total += hashmap[s[idx]]
        
        # Add the value of the last character to the total
        return total + hashmap[s[-1]]
