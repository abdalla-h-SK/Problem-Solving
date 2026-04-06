# 79
# my solution ->

#   Time : O(m * n) ^ 2
#   Space: O(len(word))

class Solution(object):
    def exist(self, board, word):
        m, n = len(board), len(board[0])
        seen = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j, index):
            seen.add((i, j))
            if index == len(word) - 1:
                return True

            for i_move, j_move in directions:
                r, c = i+i_move, j+j_move
                if 0 <= r < m and 0 <= c < n and board[r][c] == word[index+1] and (r, c) not in seen:
                    if dfs(r, c, index + 1):
                        return True

            seen.remove((i, j))
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True

        return False