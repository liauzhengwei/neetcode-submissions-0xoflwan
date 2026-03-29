class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end  # checks if the two words are of equal length and hence the same word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:   # characters are checked sequentially
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
            
    # eg. apple
    # root -> a -> p -> p -> l -> e (is_end = True)
    # root.children = {'a': TrieNode}
    # root.children['a'].children = {'p': TrieNode}
        