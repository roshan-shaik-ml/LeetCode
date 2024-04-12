"""
LeetCode [102]: Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).

Approach:
Perform a level order traversal using a queue to keep track of nodes at each level.
1. Initialize an empty queue and a list to store the result.
2. Add the root node to the queue.
3. While the queue is not empty, iterate through the nodes in the queue.
4. For each node, add its value to the current level list and enqueue its children (if any).
5. After processing all nodes at the current level, append the level list to the result list.
6. Continue until all levels are processed.
7. Finally, return the result list containing level order traversal.

Code:
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []  # List to store the result
        queue = []  # Queue for level order traversal

        # Add the root node to the queue if it exists
        if root:
            queue.append(root)

        # Perform level order traversal
        while queue:
            level = []  # List to store nodes at the current level
            # Iterate through nodes at the current level
            for _ in range(len(queue)):
                node = queue.pop(0)  # Dequeue node
                level.append(node.val)  # Add node value to current level list
                # Enqueue left and right children (if any)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(level)  # Append current level list to result list
        return ans  # Return the result list containing level order traversal
