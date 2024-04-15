/*
LeetCode [704]: Binary Search

Given a sorted (in ascending order) integer array nums of n elements and a target value, 
write a function to search target in nums. If target exists, then return its index, 
otherwise return -1.

Approach:
Perform binary search on the sorted array to find the target value. 
Keep track of the lower and upper bounds of the search range and adjust them accordingly.

Code with Comments:
*/

class Solution {
public:
    int search(vector<int>& nums, int target) {
        // Initialize lower and upper bounds of the search range
        int low = 0;
        int high = nums.size() - 1; 
        int mid;
        
        // Binary search loop
        while (low <= high) {
            // Calculate the middle index
            mid = low + (high - low) / 2;

            // If target is found, return the index
            if (nums[mid] == target)
                return mid;
            // If target is less than the middle element, search in the left half
            else if (target < nums[mid])
                high = mid - 1;
            // If target is greater than the middle element, search in the right half
            else
                low = mid + 1;
        }

        // If target is not found, return -1
        return -1;
    }
};
