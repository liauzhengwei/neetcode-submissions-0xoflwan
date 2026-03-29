class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        neg_diag = set()
        pos_diag = set()

        board = [["." for _ in range(n)] for _ in range(n)]
        res = []
        def backtrack(row):
            if row == n:
                res.append(["".join(row) for row in board])
                return

            for col in range(n):

                if (col in cols or (col + row) in pos_diag or (row - col) in neg_diag):
                    continue

                board[row][col] = 'Q'
                cols.add(col)
                neg_diag.add(row - col)
                pos_diag.add(row + col)

                backtrack(row + 1)

                board[row][col] = '.'
                cols.remove(col)
                neg_diag.remove(row - col)
                pos_diag.remove(row + col)

        backtrack(0)
        return res