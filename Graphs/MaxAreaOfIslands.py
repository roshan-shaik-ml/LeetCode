"""
LeetCode [695]: Max Area of Island

Given a grid where each cell is a land (value 1) or water (value 0), calculate the maximum area of an island. An island is formed by connecting adjacent lands horizontally or vertically.

Approach:
- We can perform a depth-first search (DFS) traversal on each land cell to explore its connected land cells and calculate the area.
- Maintain a visited matrix to keep track of visited cells to avoid counting them multiple times.
- Iterate through each cell in the grid. If the cell is land (grid[i][j] == 1) and has not been visited, perform DFS from that cell to explore the connected land cells and calculate the area of the island.
- Update the maximum area of the island as we explore each cell.

"""

from typing import List

class Solution:
    def __init__(self):
        self.result = 0
        self.visited = []

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Get the number of rows and columns in the grid
        rows, cols = len(grid), len(grid[0]) 
        # Initialize the visited matrix with False values
        self.visited = [[False] * cols for _ in range(rows)] 

        # Iterate through each cell in the grid
        for row in range(rows):
            for col in range(cols):
                # If the cell is land and has not been visited, perform DFS to explore the island
                if not self.visited[row][col] and grid[row][col] == 1:
                    # Start exploring the island from this cell
                    count = self.explore(grid, row, col, self.visited, 1)
                    # Update the maximum area of the island
                    self.result = max(count, self.result)
        
        return self.result

    def explore(self, grid, i, j, visited, count):
        # If the cell has been visited, return the count
        if self.visited[i][j]:
            return count
        
        # Mark the current cell as visited
        self.visited[i][j] = True
        # Define the directions to explore (up, down, left, right)
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        # Explore each direction
        for x, y in directions:
            # Calculate the new indices after moving in a direction
            i_new = i + x
            j_new = j + y
            # Check if the new indices are within the grid boundaries and if the cell is land and not visited
            if (0 <= i_new < len(grid) and 0 <= j_new < len(grid[0]) and 
                grid[i_new][j_new] == 1 and not visited[i_new][j_new]):
                # If the conditions are met, continue exploring the island
                count = 1 + self.explore(grid, i_new, j_new, self.visited, count)

        return count
