/**
 * LeetCode [226]: Invert Binary Tree
 * 
 * Given the root of a binary tree, invert the tree, and return its root.
 * 
 * Approach:
 * Recursively invert the left and right subtrees of each node starting from the root.
 * 
 * Code with Comments:
 */

class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        // Base case: If the root is null, return null
        if (root == nullptr)
            return nullptr;
        
        // Create a new node with the same value as the current root
        TreeNode* tempNode = new TreeNode(root->val);
        // Recursively invert the left subtree and assign it to the right child of the new node
        tempNode->left = invertTree(root->right);
        // Recursively invert the right subtree and assign it to the left child of the new node
        tempNode->right = invertTree(root->left);

        // Return the new node representing the inverted subtree
        return tempNode;
    }
};
