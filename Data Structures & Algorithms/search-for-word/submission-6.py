class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        rows, cols = len(board), len(board[0])

        def dfs(row, col, index):
            if index == len(word):
                return True

            if (row >= rows or col >= cols or row < 0 or col < 0 or word[index] != board[row][col]):
                return False

            temp = board[row][col]
            board[row][col] = "#"

            found = (dfs(row + 1, col, index+1) or 
            dfs(row, col + 1, index + 1) or
            dfs(row - 1, col, index + 1) or 
            dfs(row, col - 1, index + 1))

            board[row][col] = temp

            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j, 0):
                    return True
                
        return False