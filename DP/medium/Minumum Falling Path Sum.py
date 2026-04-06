# 931
# my solutin ->

class Solution(object):
    def minFallingPathSum(self, matrix):
        n = len(matrix)
        memo = {}
        for j in range(n):
            memo[(n-1, j)] = matrix[n-1][j]

        def minSum(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            smallest = float('inf')
            for j_off in range(j-1, j+2):
                if 0 <= j_off < n:
                    smallest = min(smallest, matrix[i][j] + minSum(i+1, j_off))
            
            memo[(i, j)] = smallest
            return smallest
        
        ans = float('inf')
        for j in range(n):
            ans = min(ans, minSum(0, j))
        
        return ans