class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        # Track occupied columns and diagonals
        cols = set()    # Column positions
        pos_diag = set()    # Positive diagonals (r + c)
        neg_diag = set()    # Negative diagonals (r - c)

        board = [['.' for _ in range(n)] for _ in range(n)]

        def backtrack(row):
            if row == n:
                # Convert board to string format
                res.append([''.join(row) for row in board])
                return 
            
            for col in range(n):
                # Check if position is under attack
                if (col in cols or (row + col) in pos_diag or
                (row - col) in neg_diag):
                    continue

                # Place queen
                board[row][col] = 'Q'
                cols.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)

                # Recurse to next row
                backtrack(row + 1)

                # Backtrack (remove queen)
                board[row][col] = '.'
                cols.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)

        backtrack(0)
        return res