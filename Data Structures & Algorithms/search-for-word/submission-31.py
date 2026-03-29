class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        rows, cols = len(board), len(board[0])

        def dfs(row, col, index):
            if index == len(word):
                return True

            if (row >= rows or col >= cols or col <0 or row < 0 or board[row][col]!= word[index]):
                return False

            tmp = board[row][col]
            board[row][col] = "."

            found = (dfs(row, col+1, index+1) 
            or dfs(row, col-1, index+1)
            or dfs(row-1, col, index+1)
            or dfs(row+1, col, index+1))

            board[row][col] = tmp

            return found

        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0):
                    return True

        return False