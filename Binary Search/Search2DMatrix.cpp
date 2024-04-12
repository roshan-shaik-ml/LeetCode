"""
LeetCode [74]: Search a 2D Matrix

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.

Approach:
1. Iterate through each row of the matrix.
2. If the target is within the range of the current row, perform a binary search on that row.
3. Return true if the target is found in any row, otherwise return false.

Code:
"""

class Solution {
public:
    // Function to search for the target value in the matrix
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        bool ans = false;
        // Iterate through each row of the matrix
        for(auto v: matrix) {
            // If the current row has only one element and it is equal to the target, return true
            if(v.size() == 1 && v.front() == target)
                return true;
            // If the target is within the range of the current row, perform binary search
            if(target >= v.front() && target <= v.back()) {
                ans = binarySearch(v, target);
            }
        }
        // Return the result
        return ans;
    }
    
    // Function to perform binary search on a sorted array
    bool binarySearch(vector<int> arr, int target) {
        int low = 0;
        int high = arr.size() - 1;
        // Binary search loop
        while(low <= high) {
            int mid = low + (high - low) / 2;
            // If target is found at mid, return true
            if(arr[mid] == target)
                return true;
            // If target is greater than mid, search in the right half
            else if(target > arr[mid])
                low = mid + 1;
            // If target is smaller than mid, search in the left half
            else if(target < arr[mid])
                high = mid - 1;   
        }
        // If target is not found, return false
        return false;
    }
};
