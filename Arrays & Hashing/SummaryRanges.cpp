/**
 * LeetCode [228]: Summary Ranges
 * 
 * Given a sorted integer array nums, return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
 * That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
 * 
 * Approach:
 * Iterate through the sorted array of integers and maintain the current range. 
 * Whenever a break in the sequence is encountered, add the current range to the result and update the range.
 * 
 * Code with Comments:
 */

class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        // Initialize an empty vector to store the result
        vector<string> ans;
        // If the input array is empty, return an empty result
        if (nums.empty()) {
            return ans;
        }

        // Initialize variables to track the previous number and the current range
        int prev = nums[0];
        string range = to_string(prev);
        int i = 1;

        // Iterate through the array starting from the second element
        while (i < nums.size()) {
            // Calculate the difference between the current and previous numbers
            long long result = (long long)nums[i] - (long long)nums[i - 1];
            // If the difference is 1, the sequence continues; update the previous number and move to the next element
            if (result == 1LL) {
                prev = nums[i];
                i++;
                continue;
            }
            // If the previous number is equal to the current range, add the single number to the result
            else if (prev == stoi(range)) {
                ans.push_back(range);
                prev = nums[i];
                range = to_string(nums[i]);
            }
            // If the previous number is not equal to the current range, add the range to the result
            else if (prev != stoi(range)) {
                // Append the range from the previous number to the current number
                range += "->" + to_string(nums[i - 1]);
                prev = nums[i];
                // Add the range to the result
                ans.push_back(range);
                // Reset the range to the current number
                range = to_string(nums[i]);
            }
            // Move to the next element
            i += 1;
        }

        // After the loop, handle the last range if needed
        if (prev == stoi(range)) {
            ans.push_back(range);
        } else if (prev != stoi(range)) {
            range += "->" + to_string(nums[i - 1]);
            ans.push_back(range);
        }
        // Return the final result
        return ans;
    }
};
