"""
LeetCode [700]: Search in a Binary Search Tree

Given the root of a binary search tree (BST) and an integer val, return the subtree rooted at node val if it exists, 
otherwise return None.

Approach:
1. Perform a binary search in the BST to find the node with the given value.
2. If the value matches the current node's value, return the node.
3. If the value is less than the current node's value, search in the left subtree.
4. If the value is greater than the current node's value, search in the right subtree.

Code with Comments:
"""

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Base case: If root is None, return None
        if not root:
            return None
        # If val matches the current node's value, return the node
        if val == root.val:
            return root
        # If val is less than the current node's value, search in the left subtree
        elif val < root.val:
            found = self.searchBST(root.left, val)
        # If val is greater than the current node's value, search in the right subtree
        else:
            found = self.searchBST(root.right, val)
        return found
