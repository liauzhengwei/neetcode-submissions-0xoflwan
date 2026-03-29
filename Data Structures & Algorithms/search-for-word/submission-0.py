class TrieNode:
    def __init__(self):
        self.children = {}
        self.isword = False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        root = TrieNode()
        node = root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isword = True

        rows = len(board)
        cols = len(board[0])

        found = [False]

        def backtrack(r,c,parent):
            if found[0]:
                return

            ch = board[r][c]
            if ch not in parent.children:
                return

            node = parent.children[ch]

            if node.isword:
                found[0] = True
                return

            board[r][c] = "#"

            for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    backtrack(nr,nc, node)

            board[r][c] = ch

            if not node.children:
                parent.children.pop(ch)

            
        for r in range(rows):
            for c in range(cols):
                backtrack(r,c,root)
                if found[0]:
                     return True

        return False













