"""
LeetCode [133]: Clone Graph

Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

Approach:
- Use Depth-First Search (DFS) to traverse the original graph and create a clone graph.
- Maintain a dictionary to map each node's value to its corresponding clone node.
- For each node in the graph, if it has not been visited before, create a clone node and add it to the dictionary.
- Recursively clone its neighbors and connect them to the clone node.
- Return the clone of the starting node of the original graph.

"""

from typing import Optional, List, Union
from collections import defaultdict

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:

    def __init__(self):
        # Dictionary to store mapping from original node value to its clone
        self.graph = defaultdict(list)

    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        # Start DFS traversal to clone the graph
        return self.dfs(node)
    
    def dfs(self, node: Optional[Node]) -> Union[None, Node]:
        # If node is None, return None
        if not node:
            return None

        # If node value is already in graph, return its corresponding clone
        if node.val in self.graph:
            return self.graph[node.val]

        # Create a clone node and add it to the graph dictionary
        clone = Node(node.val)
        self.graph[clone.val] = clone

        # Recursively clone neighbors and connect them to the clone node
        for neighbor in node.neighbors:
            clone.neighbors.append(self.dfs(neighbor))
                
        return self.graph[node.val]
