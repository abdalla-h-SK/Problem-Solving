# 289
# my solution ->

class Solution(object):
    def gameOfLife(self, board):
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                state = board[i][j]
                board[i][j] = [state] * 2

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        def search(i, j, state):
            lives = 0
            for i_move, j_move in directions:
                r, c = i + i_move, j + j_move
                if 0 <= r < m and 0 <= c < n and board[r][c][0] == 1:
                    lives += 1
            
            if not state and lives == 3:
                board[i][j][1] = 1
            
            if state and lives not in {2, 3}:
                board[i][j][1] = 0
                
        for i in range(m):
            for j in range(n):
                if board[i][j][0] == 1:
                    search(i, j, True)
                else:
                    search(i, j, False)
        
        for i in range(m):
            for j in range(n):
                board[i][j] = board[i][j][1]