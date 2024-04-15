"""
LeetCode [572]: Subtree of Another Tree

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure 
and node values of subRoot and false otherwise. A subtree of a binary tree tree is a tree that consists of a node in tree 
and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Approach:
1. Recursively check if subRoot is a subtree of root.
2. Base cases:
   - If subRoot is None, it is always a subtree.
   - If root is None but subRoot is not, it is not a subtree.
3. Recursively check if the current root and subRoot are identical trees.
4. If they are identical, return True.
5. Otherwise, recursively check if subRoot is a subtree of the left subtree or the right subtree of root.

Code with Comments:
"""

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base case: If subRoot is None, it is always a subtree
        if subRoot is None:
            return True
        # Base case: If root is None but subRoot is not, it is not a subtree
        if root is None:
            return False
        # Recursively check if subRoot is a subtree of root
        if self.checkSubTree(root, subRoot):
            return True
        # Otherwise, recursively check if subRoot is a subtree of the left or right subtree of root
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 

    def checkSubTree(self, root, subRoot):
        # Base case: If both root and subRoot are None, they are identical
        if not root and not subRoot:
            return True
        # If both root and subRoot are not None and have the same value, recursively check left and right subtrees
        elif root and subRoot and root.val == subRoot.val:
            left_sub = self.checkSubTree(root.left, subRoot.left)
            right_sub = self.checkSubTree(root.right, subRoot.right)
            return left_sub and right_sub
        # Otherwise, they are not identical
        else:
            return False
