# Create a TrieNode class with children and isword = False for the word to be found
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isword = False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        root = TrieNode()
        node = root
        # Create the TrieNode structure
        for ch in word:
            # Create a TrieNode as children to the current node with the ch in word
            if ch not in node.children:
                node.children[ch] = TrieNode()
            # Got through the TrieNode structure
            node = node.children[ch]
        # At the end, of the word, set the isword as True for that last node
        node.isword = True

        # Get the length of rows and cols
        rows = len(board)
        cols = len(board[0])

        # Set found as False
        found = [False]

        def backtrack(r,c,parent):
            # Terminate early if the word is found
            if found[0]:
                return
            
            # Get the current board character
            ch = board[r][c]
            # See if it exists in the node structure
            if ch not in parent.children:
                return

            # It exists, so get that node 
            node = parent.children[ch]

            # The word is found
            if node.isword:
                found[0] = True
                return

            # Set visited on the board
            board[r][c] = "#"

            # Go explore the 4 different directions
            for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                # Check boundaries and perform backtracking with current node
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    backtrack(nr,nc, node)

            # Reset the board to its original character
            board[r][c] = ch

            # If current node has no more children, then prune that branch
            ## means the path does not go through this node
            if not node.children:
                parent.children.pop(ch)

        # Iterate through every possible start position and pass the TrieNode structure
        for r in range(rows):
            for c in range(cols):
                backtrack(r,c,root)
                if found[0]:
                     return True

        return False













