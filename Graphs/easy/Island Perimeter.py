# 463
# my solution ->
from collections import deque

class Solution(object):
    def islandPerimeter(self, grid):
        m, n = len(grid), len(grid[0])
        self.perimeter = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        seen = set()
        que = deque()

        def bfs():
            while que:
                i, j = que.popleft()
                self.perimeter += 4
                for i_off, j_off in directions:
                    r, c = i + i_off, j + j_off
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                        self.perimeter -= 1
                        if (r, c) not in seen:
                            que.append((r, c))
                            seen.add((r, c))
        
        for i in range(m):
            found = False
            for j in range(n):
                if grid[i][j] == 1:
                    que.append((i, j))
                    seen.add((i, j))
                    bfs()
                    found = True
                    break
            if found:
                break
        
        return self.perimeter
    

# another simpler solution once u understand the main concept!

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        perimeter = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:

                    perimeter += 4

                    if i > 0 and grid[i - 1][j] == 1:
                        perimeter -= 2
                    if j > 0 and grid[i][j - 1] == 1:
                        perimeter -= 2

        return perimeter