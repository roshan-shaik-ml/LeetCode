"""
LeetCode [100]: Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Approach:
Perform a depth-first search (DFS) traversal of both trees simultaneously and compare their nodes.
1. If both nodes are None, return True as they are considered equal.
2. If one node is None and the other is not, return False as they are not equal.
3. If both nodes have values and they are equal, recursively check their left and right subtrees.
4. If the values of the nodes are not equal, return False.
5. Finally, return the result of both subtree comparisons.

Code:
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case: If both nodes are None, they are equal
        if not p and not q:
            return True
        # If one node is None and the other is not, they are not equal
        if not p or not q:
            return False
        # If the values of both nodes are equal, recursively check left and right subtrees
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # If the values of the nodes are not equal, they are not equal
        return False
