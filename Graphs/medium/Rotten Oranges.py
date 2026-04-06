# 994
# my solution ->

    # Time : O(m * n)
    # Space: O(m * n)

from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        m, n = len(grid), len(grid[0])

        rotten = deque()
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        minutes = 0
        while fresh and rotten:
            k = len(rotten)
            for i in range(k):
                i, j = rotten.popleft()

                if j < n-1 and grid[i][j+1] == 1:
                    rotten.append((i,j+1))
                    grid[i][j+1] = 2
                    fresh -= 1

                if i < m-1 and grid[i+1][j] == 1:
                    rotten.append((i+1,j))
                    grid[i+1][j] = 2
                    fresh -= 1

                if grid[i][j-1] == 1 and j > 0:
                    rotten.append((i, j-1))
                    grid[i][j-1] = 2
                    fresh -= 1

                if grid[i-1][j] == 1 and i > 0:
                    rotten.append((i-1,j))
                    grid[i-1][j] = 2
                    fresh -= 1

            minutes += 1

        return minutes if not fresh else -1