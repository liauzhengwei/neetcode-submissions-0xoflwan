class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        rows, cols = len(board), len(board[0])

        def dfs(row, col, index):
            # Found the entire word
            if index == len(word):
                return True

            # Check boundaries and character match
            if (row < 0 or row >= rows 
            or col < 0 or col >= cols
            or word[index] != board[row][col]):
                return False

            # Mark current cell as visited
            temp = board[row][col]
            board[row][col] = '#'

            # Explore all 4 directions
            found = (dfs(row + 1, col, index + 1) or
            dfs(row - 1, col, index + 1) or
            dfs(row, col + 1, index + 1) or
            dfs(row, col - 1, index + 1))

            # Backtrack: restore the cell
            board[row][col] = temp
            return found

        # Try starting from each cell
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False