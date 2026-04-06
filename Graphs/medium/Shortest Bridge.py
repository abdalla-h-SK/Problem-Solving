# 934
# my solution ->
from collections import deque

class Solution(object):
    def shortestBridge(self, grid):
        m, n = len(grid), len(grid[0])
        que = deque()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def prepare_que(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
                return
            else:
                grid[i][j] = 2
                for i_off, j_off in  directions:
                    r, c = i + i_off, j + j_off
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == 0:
                        que.append(((i, j), 0))
                        break

                prepare_que(i, j+1)
                prepare_que(i+1, j)
                prepare_que(i, j-1)
                prepare_que(i-1, j)

                
        for i in range(m):
            found = False
            for j in range(n):
                if grid[i][j] == 1:
                    prepare_que(i, j)
                    found = True
                    break
            if found:
                break

        while que:
            for _ in range(len(que)):
                dim, length = que.popleft()
                i, j = dim[0], dim[1]

                for i_off, j_off in  directions:
                    r, c = i + i_off, j + j_off
                    if 0 <= r < m and 0 <= c < n:
                        if grid[r][c] == 0:
                            grid[r][c] = 2
                            que.append(((r, c), length + 1))
                        
                        elif grid[r][c] == 1:
                            return length