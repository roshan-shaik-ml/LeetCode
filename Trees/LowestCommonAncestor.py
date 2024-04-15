"""
LeetCode [235]: Lowest Common Ancestor of a Binary Search Tree

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

Approach:
Traverse the BST starting from the root node. At each node, compare the values of the two given nodes with the current node's value to determine the direction to move next:
- If both nodes' values are smaller than the current node's value, move to the left subtree.
- If both nodes' values are greater than the current node's value, move to the right subtree.
- Otherwise, the current node is the lowest common ancestor.

Code with Comments:
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Initialize the LCA to the root node
        LCA = root
        
        # Traverse the BST to find the LCA
        while True:
            # If both nodes are smaller than the current node, move to the left subtree
            if p.val < LCA.val and q.val < LCA.val:
                LCA = LCA.left
            # If both nodes are greater than the current node, move to the right subtree
            elif p.val > LCA.val and q.val > LCA.val:
                LCA = LCA.right
            # Otherwise, the current node is the LCA
            else:
                return LCA
