/**
 * LeetCode [112]: Path Sum
 * 
 * Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
 * 
 * Approach:
 * Recursively check if there exists a path from the root to a leaf node such that the sum of values along the path equals the targetSum.
 * 
 * Code:
 */

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool hasPathSum(TreeNode* root, int targetSum) {
        // Base case: If the root is null, return false
        if(root == nullptr)
            return false;

        bool right = false, left = false;

        // Update the targetSum by subtracting the value of the current node
        targetSum -= root->val;

        // If the current node is a leaf and its value equals the remaining targetSum, return true
        if(targetSum == 0 && root->left == nullptr && root->right == nullptr)
            return true;
        
        // Recursively check the right subtree if it exists
        if(root->right != nullptr)
            right = hasPathSum(root->right, targetSum);
        
        // Recursively check the left subtree if it exists
        if(root->left != nullptr)
            left = hasPathSum(root->left, targetSum);

        // Return true if there exists a path sum in either the left or right subtree
        return (right || left); 
    }
};
