# 1926
# The trick here is that BFS takes less time than dfs as it gives time limit exceeded!

from collections import deque
class Solution(object):
    def nearestExit(self, maze, entrance):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        queue = deque([(entrance[0], entrance[1], 0)])
        
        maze[entrance[0]][entrance[1]] = '+'
        
        while queue:
            row, col, steps = queue.popleft()

            if (row == 0 or row == len(maze) - 1 or col == 0 or col == len(maze[0]) - 1) and [row, col] != entrance:
                return steps
            
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] == '.':
                    maze[new_row][new_col] = '+'
                    queue.append((new_row, new_col, steps + 1))
        
        return -1