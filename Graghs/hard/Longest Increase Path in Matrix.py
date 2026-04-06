# 329
class Solution(object):
    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0
        
        m, n = len(matrix), len(matrix[0])

        paths_dict = {}

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(i, j):

            if (i, j) in paths_dict:
                return paths_dict[(i, j)]

            longest = 1

            for di, dj in directions:
                ni, nj = i + di, j + dj

                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    longest = max(longest, 1 + dfs(ni, nj))

            paths_dict[(i, j)] = longest
            return longest

        max_path = 0
        for i in range(m):
            for j in range(n):
                max_path = max(max_path, dfs(i, j))
        
        return max_path
    

# Not too bad
class Solution(object):
    def longestIncreasingPath(self, matrix):
        m, n = len(matrix), len(matrix[0])
        max_path = [0]
        absolute_max = [0]
        paths_dict = {}

        def dfs(i, j, prev, path_sum):
            if i < 0 or i >= m or j < 0 or j >= n or prev and matrix[i][j] <= prev:
                return
            elif ((i, j)) in paths_dict:
                path_sum += paths_dict[(i, j)]
                max_path[0] = max(max_path[0], path_sum)
                absolute_max[0] = max(max_path[0], absolute_max[0])
                return
            else:
                path_sum += 1
                max_path[0] = max(max_path[0], path_sum)
                absolute_max[0] = max(max_path[0], absolute_max[0])
                prev = matrix[i][j]
                
                dfs(i, j+1, prev, path_sum)
                dfs(i-1, j, prev, path_sum)
                dfs(i, j-1, prev, path_sum)
                dfs(i+1, j, prev, path_sum)

                paths_dict[(i, j)] = max_path[0] - path_sum + 1
                
        
        for i in range(m):
            for j in range(n):
                max_path[0] = 0
                dfs(i, j, None, 0)
        return absolute_max[0]