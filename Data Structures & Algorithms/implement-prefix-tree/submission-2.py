# Trie is used for storing strings for 1. inserting words 2. searching words 3. checking prefixes
## Each Node is a character, links to next characters, has flag of whether end of word

class TrieNode:
    def __init__(self):
        self.children = {}  # char -> TrieNode
        self.end = False    # marks end of word


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

        node.end = True

    # Full match
    def search(self, word: str) -> bool:
        node = self.root

        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        
        return node.end


    # Prefix match
    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]

        return True
        