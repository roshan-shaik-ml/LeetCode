/*
LeetCode [3]: Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Approach:
1. Initialize a sliding window using two pointers: 'left' and 'right'.
2. Use a hash set to store unique characters within the current substring.
3. Iterate through the string using the sliding window approach.
4. At each step, check if the character at the 'right' pointer is already in the hash set.
   - If not, add it to the hash set and update the answer if needed.
   - If yes, remove the character at the 'left' pointer from the hash set and move the 'left' pointer to the right.
5. Move the 'right' pointer to expand the window.
6. Repeat steps 4-5 until the 'right' pointer reaches the end of the string.
7. Return the length of the longest substring found.
*/

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // Check if the input string is empty
        if(s.size() == 0) 
            return 0;

        // Create an unordered set to store unique characters
        unordered_set<char> hashset;
        // Initialize pointers for the sliding window
        int left = 0;
        int right = 1;
        // Insert the first character into the set
        hashset.insert(s[left]);
        // Initialize variables to track the answer and current substring length
        int ans = 1;
        int len = 0;

        // Iterate through the string using a sliding window approach
        while(right < s.size()) {
            // Get the characters at the left and right pointers
            char right_chr = s[right];
            char left_chr = s[left];
            // Calculate the length of the current substring
            len = right - left + 1;
            // If the right character is not in the set, insert it and update the answer
            if(hashset.find(right_chr) == hashset.end()) {
                hashset.insert(right_chr);
                ans = max(len, ans);
            }
            // If the right character is already in the set, move the left pointer
            else if(hashset.find(right_chr) != hashset.end()) {
                hashset.erase(s[left]);
                left++;
                continue;
            }
            // Move the right pointer to expand the window
            right++;
        }
        // Return the length of the longest substring
        return ans;
    }
};
