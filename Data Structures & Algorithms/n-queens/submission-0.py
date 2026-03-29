class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # use backtracking

        # Create a board made of "."
        board = [["."] * n for _ in range(n)]

        def is_safe(row, col):
            # Check columns if previously filled
            for i in range(row):
                if board[i][col] == "Q":
                    return False

            # Check if top right diagonal previously filled
            i, j = row - 1, col - 1
            while i>=0 and j>=0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            # Check if top left diagonal previously filled
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1
            return True

        def backtrack(row):
            if row == n:
                # Found a valid arrangement
                result.append(["".join(r) for r in board])
                return 

            # Check for every column if queen can be added
            for col in range(n):
                if is_safe(row, col):
                    # If is safe to assign, then assign 
                    board[row][col] = "Q"
                    # Go to the next row
                    backtrack(row + 1)
                    # Reset the value to "."
                    board[row][col] = "." 


        result = []
        backtrack(0)
        return result