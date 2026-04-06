# 2352
# my solution ->

from collections import defaultdict
class Solution(object):
    def equalPairs(self, grid):
        m, n = len(grid), len(grid[0])
        rows = defaultdict(int)
        colomns = defaultdict(int)

        for row in grid:
            rows[tuple(row)] += 1
        
        for j in range(n):
            tpl = []
            for i in range(m):
                tpl.append(grid[i][j])
            colomns[tuple(tpl)] += 1
        
        ans = 0
        commons = [puplic for puplic in rows if puplic in colomns]
        for puplic in commons:
            ans += rows[puplic] * colomns[puplic]
        
        return ans