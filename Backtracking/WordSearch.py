"""
LeetCode [79]: Word Search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

Approach:
1. Check if the board has enough letters to form the word. If not, return False.
2. Check if the board has the required number of each letter for the word. If not, return False.
3. Implement Depth-First Search (DFS) to search for the word in the board:
   - Start DFS from each cell in the board.
   - At each cell, check if the current letter matches the first letter of the word.
   - If yes, recursively search for the remaining letters in all four directions (up, down, left, right).
   - Mark the visited cells to avoid revisiting them during the search.
4. Return True if the word is found starting from any cell, otherwise return False.

Code:
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        # If the board doesn't have enough letters, return false
        if len(word) > rows * cols:
            return False
        # If the board doesn't have required number of each letter, return false
        board_letter_counts = Counter(chain.from_iterable(board))
        word_letter_counts = Counter(word)
        for letter, count in word_letter_counts.items():
            if count > board_letter_counts[letter]:
                return False
        # Go for the DFS approach
        visited = [[False for i in range(0, len(board[0]))] for j in range(0, len(board))]
        for row in range(0, rows):
            for col in range(0, cols):
                if board[row][col] == word[0]:
                    ans = self.search(board, row, col, word, 0, visited)
                    if ans == True:
                        return True
        return False
    
    # Function to perform DFS search for the word in the board
    def search(self, board, row, col, word, idx, visited):
        visited[row][col] = True
        if (idx + 1) == len(word):
            return True
        offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for x, y in offsets:
            new_row = row + x
            new_col = col + y
            x_boundary = new_row >= 0 and new_row < len(board)
            y_boundary = new_col >= 0 and new_col < len(board[0])   
            if (x_boundary and y_boundary and not visited[new_row][new_col] 
            and word[idx+1] == board[new_row][new_col]):
                ans = self.search(board, new_row, new_col, word, idx+1, visited)
                if ans:
                    return True
        visited[row][col] = False 
        # Reset the visited matrix for backtracking
        # As the previously visited cells could be a part of the final solution
        # But not the current path that has been explored.
        return False
