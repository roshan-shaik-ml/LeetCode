"""
LeetCode [701]: Insert into a Binary Search Tree

Given the root node of a binary search tree (BST) and a value to insert into the tree, 
insert the value into the BST. Return the root node of the BST after the insertion. 
It is guaranteed that the new value does not exist in the original BST.

Approach:
1. Recursively traverse the BST.
2. If the current node is None, create a new node with the given value and return it.
3. If the value to be inserted is less than the current node's value, insert it into the left subtree.
4. If the value to be inserted is greater than or equal to the current node's value, insert it into the right subtree.

Code with Comments:
"""

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Base case: If root is None, create a new node with the given value and return it
        if not root:
            root = TreeNode(val)
            return root
        # If the value to insert is less than the current node's value, insert into the left subtree
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        # If the value to insert is greater than or equal to the current node's value, insert into the right subtree
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root
