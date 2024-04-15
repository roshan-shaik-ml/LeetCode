/*
LeetCode [283]: Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Approach:
1. Initialize two pointers, front and back, both starting from the beginning of the array.
2. Iterate through the array with the front pointer:
   - If the element at front pointer is non-zero and the element at back pointer is zero, swap them.
   - Move both front and back pointers forward.
3. If the element at back pointer is non-zero, move the back pointer forward.
4. Continue until the front pointer reaches the end of the array.

Code with Comments:
*/

#include <vector>
using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) return;

        int front = 1;
        int back = 0;

        // Iterate through the array with front pointer
        while (front < n) {
            // If front element is non-zero and back element is zero, swap them
            if (nums[front] != 0 && nums[back] == 0) {
                int temp = nums[front];
                nums[front] = nums[back];
                nums[back] = temp;
                back++;
            }
            // If back element is non-zero, move back pointer forward
            if (nums[back] != 0) back++;
            // Move front pointer forward
            front++;
        }
    }
};
