"""
LeetCode [230]: Kth Smallest Element in a BST

Given the root of a binary search tree (BST), and an integer k, return the kth (1-indexed) smallest element in the BST.

Approach:
Perform an inorder traversal of the BST to get the elements in ascending order. As the inorder traversal of a BST gives elements in sorted order, we can retrieve the kth smallest element by accessing the element at index k-1 in the traversal result.

Code with Comments:
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Perform an inorder traversal to get the elements in sorted order
        stack = self.inorder(root, [])
        # Return the kth element (1-indexed) from the sorted list
        return stack[k - 1]
    
    def inorder(self, root, stack):
        # Recursive function to perform inorder traversal
        if root:
            # Traverse the left subtree
            self.inorder(root.left, stack)
            # Append the current node's value to the stack
            stack.append(root.val)
            # Traverse the right subtree
            self.inorder(root.right, stack)
        # Return the stack containing elements in sorted order
        return stack
