"""
LeetCode [145]: Binary Tree Postorder Traversal

Given the root of a binary tree, return the postorder traversal of its nodes' values.

Approach:
Perform a postorder traversal of the binary tree recursively:
1. Recursively traverse the left subtree.
2. Recursively traverse the right subtree.
3. Visit the current node.

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
        # Initialize a list to store the postorder traversal result
        self.ans = []

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Perform a postorder traversal recursively
        if root:
            # Recursively traverse the left subtree
            self.postorderTraversal(root.left)
            # Recursively traverse the right subtree
            self.postorderTraversal(root.right)
            # Visit the current node and append its value to the result list
            self.ans.append(root.val)
        
        # Return the list containing the postorder traversal result
        return self.ans
