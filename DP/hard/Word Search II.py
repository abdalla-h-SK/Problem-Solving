# 212

class Solution(object):
    def findWords(self, board, words):
        self.trie = {}
        for word in words:
            d = self.trie
            for c in word:
                if c not in d:
                    d[c] = {}
                d = d[c]
            
            d['.'] = '.'

        res, seen = set(), set()
        m, n = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(i, j, d, word):
            if '.' in d:
                res.add(word)
                
            seen.add((i, j))
            for i_off, j_off in directions:
                r, c = i+i_off, j+j_off
                if 0 <= r < m and 0 <= c < n and board[r][c] in d and (r, c) not in seen:
                    dfs(r, c, d[board[r][c]], word + board[r][c])
            seen.remove((i, j))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] in self.trie:
                    dfs(i, j, self.trie[board[i][j]], board[i][j])
        
        return list(res)