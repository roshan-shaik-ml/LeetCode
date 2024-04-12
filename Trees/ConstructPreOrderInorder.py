"""
LeetCode [105]: Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversal of a tree, construct the binary tree.

Example:
Input:
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

Output:
    3
   / \
  9  20
    /  \
   15   7

Approach:
1. The first element in the preorder list is the root of the current subtree.
2. Find the index of the root element in the inorder list to determine the left and right subtrees.
3. Recursively build the left subtree using the elements to the left of the root in the inorder list and the corresponding elements in the preorder list.
4. Recursively build the right subtree using the elements to the right of the root in the inorder list and the corresponding elements in the preorder list.
5. Return the root of the subtree.

Code:
"""

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        # Root is always the first number of preorder traversal
        root_value = preorder.pop(0)

        # Finding the root node position in inorder to split left and right
        root_idx = inorder.index(root_value)
        inorder_left, inorder_right = inorder[:root_idx], inorder[root_idx+1:]

        # Split preorder into left and right children based on the number of elements in the inorder_left
        preorder_left, preorder_right = preorder[:len(inorder_left)], preorder[len(inorder_left):]

        # Create the root node
        node = TreeNode(root_value)
        
        # Recursively build the left subtree
        node.left = self.buildTree(preorder_left, inorder_left)
        
        # Recursively build the right subtree
        node.right = self.buildTree(preorder_right, inorder_right)

        return node
