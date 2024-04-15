/**
 * LeetCode [136]: Single Number
 * 
 * Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
 * You must implement a solution with a linear runtime complexity and use only constant extra space.
 * 
 * Approach:
 * The XOR operation has the property that if we XOR two identical numbers, the result is 0.
 * Therefore, if we XOR all elements in the array, the duplicate numbers will cancel out each other,
 * leaving only the single number that appears once.
 * 
 * Code with Comments:
 */

class Solution {
public:
    int singleNumber(vector<int>& nums) {

        int result = 0;
        
        for (int num : nums) {
            // Perform XOR operation with each element
            // This effectively cancels out duplicate numbers
            result ^= num;
        }
        // The result will be the single number that appears only once
        return result;
    }
};
