"""
LeetCode [98]: Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

Approach:
Perform a depth-first search (DFS) traversal of the binary tree while keeping track of the valid range for each node.
1. Initialize a flag 'answer' to True.
2. Define a helper function 'solve' that performs a DFS traversal of the binary tree.
3. In the 'solve' function, if the current node's value falls within the valid range (defined by the parent node), recursively call 'solve' for its left and right children with updated valid ranges.
4. If the current node's value violates the valid range, set the 'answer' flag to False.
5. Finally, return the value of the 'answer' flag.

Code:
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.answer = True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Call the helper function to perform DFS traversal
        self.solve(root, -float('inf'), float('inf'))
        return self.answer
    
    def solve(self, root, left, right):
        if not root:
            return 

        # Check if the current node's value falls within the valid range
        if root.val < right and root.val > left:
            # Recursively call solve for left and right children with updated valid ranges
            self.solve(root.left, left, root.val)
            self.solve(root.right, root.val, right)
        else:
            # If the current node's value violates the valid range, set the answer flag to False
            self.answer = False
            return
