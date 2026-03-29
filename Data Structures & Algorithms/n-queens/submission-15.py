class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos_diag = set()
        neg_diag = set()

        board = [["." for _ in range(n)] for _ in range(n)]
        res = []
        def bt(row):
            if row == n:
                res.append([''.join(row) for row in board])
                return 

            for col in range(n):
                if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                    continue

                board[row][col] = 'Q'
                cols.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)

                bt(row + 1)

                board[row][col] = '.'
                cols.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)
        bt(0)
        return res