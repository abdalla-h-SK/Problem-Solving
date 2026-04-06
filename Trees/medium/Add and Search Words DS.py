# 211

class WordDictionary(object):

    def __init__(self):
        self.trie = {}

    def addWord(self, word):
        d = self.trie

        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        
        d['*'] = '*'
        

    def search(self, word):
        def dfs(d, i):
            if i == len(word):
                return '*' in d

            c = word[i]
            
            if c == '.':
                return any(dfs(d[ltr], i + 1) for ltr in d if ltr != '*')
            else:
                return c in d and dfs(d[c], i + 1)

        return dfs(self.trie, 0)