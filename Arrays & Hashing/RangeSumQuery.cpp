/*
LeetCode [303]: Range Sum Query - Immutable

Given an integer array nums, find the sum of the elements between indices left and right inclusive, where (left <= right).

Approach:
1. Use a prefix sum array to store the cumulative sum up to each index.
2. Initialize the prefix sum array with the cumulative sum of the input array.
3. To find the sum between left and right indices, subtract the prefix sum at left-1 index from the prefix sum at right index.

Code with Comments:
*/

#include <vector>
using namespace std;

class NumArray {
public:
    vector<int> prefix;

    // Constructor to initialize prefix sum array
    NumArray(vector<int>& nums) {
        int n = nums.size();
        prefix.push_back(nums[0]);
        for (int i = 1; i < n; i++) {
            prefix.push_back(prefix.back() + nums[i]);
        }
    }
    
    // Function to return the sum between left and right indices
    int sumRange(int left, int right) {
        if (left == 0)
            return prefix[right];
        return (prefix[right] - prefix[left - 1]);
    }
};

// Your NumArray object will be instantiated and called as such:
// NumArray* obj = new NumArray(nums);
// int param_1 = obj->sumRange(left, right);
