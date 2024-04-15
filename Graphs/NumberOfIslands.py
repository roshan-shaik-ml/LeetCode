"""
LeetCode [200]: Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

Approach:
Iterate through each cell of the grid. When encountering a '1' that has not been visited, mark it as visited and recursively explore all adjacent '1's to form an island. Count each island encountered.

Code with Comments:
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Initialize the count of islands
        islands = 0
        # Get the number of rows and columns in the grid
        rows, cols = len(grid), len(grid[0])
        # Initialize a matrix to keep track of visited cells
        visited = [[False] * cols for _ in range(rows)]
        # Iterate through each cell of the grid
        for row in range(rows):
            for col in range(cols):
                # If the cell contains '1' and has not been visited yet
                if grid[row][col] == '1' and not visited[row][col]:
                    # Increment the count of islands
                    islands += 1
                    # Recursively explore all adjacent '1's to form an island
                    self.explore(grid, visited, row, col)
        # Return the total count of islands
        return islands
    
    # Helper function to explore adjacent cells recursively
    def explore(self, grid, visited, row, col):
        # Mark the current cell as visited
        visited[row][col] = True
        # Define offsets to explore adjacent cells
        offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        # Iterate through each offset
        for x, y in offsets:
            new_x, new_y = row + x, col + y
            # Check if the new coordinates are within bounds and the cell contains '1' and has not been visited
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == '1' and not visited[new_x][new_y]:
                # Recursively explore the adjacent cell
                self.explore(grid, visited, new_x, new_y)
