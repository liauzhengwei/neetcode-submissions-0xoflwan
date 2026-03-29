class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        
        rows, cols = len(board), len(board[0])

        def bt(row, col, index):
            if len(word) == index:
                return True

            if (row >= rows or col >= cols or col < 0 or row < 0 or word[index] != board[row][col]):
                return False
            tmp = board[row][col]
            board[row][col] = "."

            found = (bt(row + 1, col, index+1) or
            bt(row - 1, col, index + 1) or 
            bt(row, col + 1, index + 1) or
            bt(row, col - 1, index + 1))

            board[row][col] = tmp

            return found

        for i in range(rows):
            for j in range(cols):
                if bt(i,j,0):
                    return True
        
        return False



