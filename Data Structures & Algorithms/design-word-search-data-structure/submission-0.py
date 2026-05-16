class WordDictionary:

    def __init__(self):
        self.trie = dict()        

    def addWord(self, word: str) -> None:
        d = self.trie

        for c in word:
            if c not in d:
                d[c] = dict()
            d = d[c]
        d['*'] = '*'        

    def search(self, word: str) -> bool:
        return self._search_helper(word, 0, self.trie)
    
    def _search_helper(self, word, index, node):
        if index == len(word):
            return '*' in node
        char = word[index]

        if char == '.':
            for c in node.values():
                if isinstance(c, dict) and self._search_helper(word, index + 1, c):
                    return True
            return False
        elif char in node:
            return self._search_helper(word, index + 1, node[char])
        else:
            return False        
