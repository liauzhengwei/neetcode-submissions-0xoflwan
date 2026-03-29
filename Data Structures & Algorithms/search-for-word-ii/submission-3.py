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
        result = []

        def backtrack(r,c,parent):
            ch = board[r][c]
            if ch not in parent.children:
                return
            node = parent.children[ch]

            # Found a word
            if node.word:
                result.append(node.word)
                node.word = None # avoid duplicates

            # Mark visited
            board[r][c] = "#"

            # Explore neighbours (up,down,left,right)
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc = r + dr, c + dc
                if 0<= nr < rows and 0 <= nc < cols and board[nr][nc]!="#":
                    backtrack(nr,nc,node)

            # Restore cell after search
            board[r][c] = ch

            # Optimization: prune dead branches
            if not node.children:
                parent.children.pop(ch)

        # Start DFS from each cell
        for r in range(rows):
            for c in range(cols):
                backtrack(r,c,root)

        return result
                