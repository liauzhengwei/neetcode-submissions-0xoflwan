class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]

            node.word = word

        rows, cols = len(board), len(board[0])

        res = []

        def dfs(r,c,node):
            ch = board[r][c]

            if ch not in node.children:
                return

            node = node.children[ch]
            
            if node.word:
                res.append(node.word)
                node.word = None

            board[r][c] = '#'

            for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr,nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr,nc,node)

            board[r][c] = ch


        for i in range(rows):
            for j in range(cols):
                dfs(i,j,root)

        return res