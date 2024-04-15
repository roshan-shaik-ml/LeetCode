/*
LeetCode [344]: Reverse String

Write a function that reverses a string. The input string is given as an array of characters s.

Approach:
Iterate through the array from both ends simultaneously, swapping characters until reaching the middle.

Code with Comments:
*/

#include <vector>

class Solution {
public:
    void reverseString(std::vector<char>& s) {
        int n = s.size();
        // Iterate through the array from both ends simultaneously
        for (int i = 0; i < n / 2; i++) {
            // Swap characters at positions i and n - i - 1
            char temp = s[i];
            s[i] = s[n - i - 1];
            s[n - i - 1] = temp;
        }
    }
};
