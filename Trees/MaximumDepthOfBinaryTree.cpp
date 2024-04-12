/**
 * LeetCode [104]: Maximum Depth of Binary Tree
 * 
 * Given the root of a binary tree, return its maximum depth.
 * A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
 * 
 * Approach:
 * Recursively calculate the maximum depth of the left and right subtrees, and return the maximum of the two depths plus one (to account for the current node).
 * 1. If the root is null, return 0.
 * 2. Recursively calculate the maximum depth of the left subtree.
 * 3. Recursively calculate the maximum depth of the right subtree.
 * 4. Return the maximum of the left and right depths plus one.
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
    int maxDepth(TreeNode* root) {
        // If the root is null, return 0
        if(root == nullptr)
            return 0;
        
        // Recursively calculate the maximum depth of the left and right subtrees
        int left = maxDepth(root->left);
        int right = maxDepth(root->right);

        // Return the maximum of the left and right depths plus one
        return max(left, right) + 1;
    }
};
