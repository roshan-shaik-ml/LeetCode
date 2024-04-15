/*
LeetCode [383]: Ransom Note

Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Approach:
1. Use two unordered maps to store the character counts of each character in ransomNote and magazine.
2. Iterate through the characters of ransomNote and magazine, and populate their respective maps with the character counts.
3. Iterate through the characters of ransomNote and check if each character count in magazine is sufficient to construct ransomNote.

Code with Comments:
*/

#include <unordered_map>
#include <string>

class Solution {
public:
    bool canConstruct(std::string ransomNote, std::string magazine) {
        // Initialize unordered maps to store character counts
        std::unordered_map<char, int> rn;
        std::unordered_map<char, int> mag;

        // Populate the map for ransomNote
        for (auto ch : ransomNote) {
            rn[ch]++;
        }

        // Populate the map for magazine
        for (auto ch : magazine) {
            mag[ch]++;
        }

        // Check if ransomNote can be constructed from magazine
        for (auto ch : ransomNote) {
            // If the character is not present in magazine or the count is insufficient, return false
            if (mag.find(ch) == mag.end() || mag[ch] < rn[ch]) {
                return false;
            }
        }
        return true;
    }
};
