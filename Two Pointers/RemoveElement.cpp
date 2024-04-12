/**
 * LeetCode [27]: Remove Element
 * 
 * Given an integer array 'nums' and an integer 'val', remove all occurrences of 'val' in 'nums' in-place. The relative order of the elements may be changed.
 * 
 * Approach:
 * 1. Initialize two pointers, 'fptr' (front pointer) and 'bptr' (back pointer), at the beginning and end of the array respectively.
 * 2. Initialize a variable 'count' to keep track of the number of occurrences of 'val'.
 * 3. Iterate through the array using a loop until 'fptr' is less than or equal to 'bptr'.
 * 4. If the element at 'bptr' is equal to 'val', increment 'count' and move 'bptr' to the left.
 * 5. If the element at 'fptr' is equal to 'val', increment 'count', swap the element at 'fptr' with the element at 'bptr', and move 'bptr' to the left.
 * 6. Move 'fptr' to the right.
 * 7. Return the size of the array minus 'count', which represents the number of elements remaining after removing all occurrences of 'val'.
 */

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        // Initialize two pointers, 'fptr' and 'bptr', at the beginning and end of the array respectively
        int fptr = 0;
        int bptr = nums.size() - 1;
        // Initialize a variable to keep track of the number of occurrences of 'val'
        int count = 0;
        
        // Iterate through the array until 'fptr' is less than or equal to 'bptr'
        while (fptr <= bptr) {
            // If the element at 'bptr' is equal to 'val', increment 'count' and move 'bptr' to the left
            if (nums[bptr] == val) {
                count++;
                bptr--;
                continue;
            }
            // If the element at 'fptr' is equal to 'val', increment 'count',
            // swap the element at 'fptr' with the element at 'bptr', and move 'bptr' to the left
            if (nums[fptr] == val) {
                count++;
                nums[fptr] = nums[bptr];
                nums[bptr] = val;
                bptr--;
            }
            // Move 'fptr' to the right
            fptr++;
        }
        // Return the size of the array minus 'count'
        return nums.size() - count;
    }
};
