/*
LeetCode [35]: Search Insert Position

Given a sorted array of distinct integers 'nums' and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Approach:
1. Initialize 'low' and 'high' pointers to the start and end of the array respectively.
2. Perform binary search to find the index of the target in the array.
3. If the target is found, return the index.
4. If the target is not found, return the value of 'low' pointer.

Code:
*/

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        // Initialize 'low' and 'high' pointers
        int low = 0;
        int high = nums.size() - 1;
        
        // Binary search loop
        while(low <= high) {
            // Calculate mid index
            int mid = (high + low) / 2;

            // If target is found, return the index
            if(target == nums[mid])
                return mid;
            // If target is less than nums[mid], update 'high'
            if(target < nums[mid])
                high = mid - 1;
            // If target is greater than nums[mid], update 'low'
            else if(target > nums[mid]) 
                low = mid + 1;
        }

        // If target is not found, return the value of 'low' pointer
        return low;
    }
};
