"""
LeetCode [144]: Binary Tree Preorder Traversal

Given the root of a binary tree, return the preorder traversal of its nodes' values.

Approach:
Perform a preorder traversal of the binary tree recursively:
1. Visit the current node.
2. Recursively traverse the left subtree.
3. Recursively traverse the right subtree.

Code with Comments:
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = []
        
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Initialize a list to store the preorder traversal result
        
        # Perform a preorder traversal recursively
        if root:
            # Visit the current node
            self.ans.append(root.val)
            # Recursively traverse the left subtree
            self.preorderTraversal(root.left)
            # Recursively traverse the right subtree
            self.preorderTraversal(root.right)
        
        # Return the list containing the preorder traversal result
        return self.ans
