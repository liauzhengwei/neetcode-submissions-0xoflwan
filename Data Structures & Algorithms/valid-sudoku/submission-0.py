class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        for i in range(9):
            row = set()
            col = set()

            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row:
                        return False
                    row.add(board[i][j])
             
                if board[j][i] != ".":
                    if board[j][i] in col:
                        return False    
                    col.add(board[j][i])

        for box_row in range(0,9,3):
            for col_row in range(0,9,3):
                seen = set()

                for i in range(3):
                    for j in range(3):
                        val = board[box_row+i][col_row+j]
                        if val != ".":
                            if val in seen:
                                return False
                            seen.add(val)

        return True
