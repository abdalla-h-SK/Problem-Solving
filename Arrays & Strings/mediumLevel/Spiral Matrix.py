# 54

# my solution ->

#   time : O(n * m)
#   space: O(n * m)

class Solution(object):
    def spiralOrder(self, matrix):

        output = []

        if not matrix or not matrix[0]:
            return output

        if len(matrix[0]) == 1:
            for arr in matrix:
                output.append(arr[0])
            return output       

        if len(matrix) == 1 :
            for item in matrix[0]:
                output.append(item)
            return output
        
        for item in matrix[0]:
                output.append(item)
        
        for i in range(1, len(matrix) -1):
            output.append(matrix[i][-1])
        
        for item in matrix[-1][::-1]:
                output.append(item)

        for i in range(len(matrix) - 2, 0, -1):
                output.append(matrix[i][0])

        new_matrix = matrix[1:-1]
 
        for arr in new_matrix:
            arr.pop(0)
            arr.pop(-1)

        return output + self.spiralOrder(new_matrix)
    
# another solution ->

#   time : O(n * m)
#   space: O(n * m)

class Solution(object):
    def spiralOrder(self, matrix):
         
        m, n = len(matrix), len(matrix[0])
        ans = []
        i, j = 0, 0
        UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
        direction = RIGHT

        UP_WALL = 0
        RIGHT_WALL = n
        DOWN_WALL = m
        LEFT_WALL = -1

        while len(ans) != m*n:
            if direction == RIGHT:
                while j < RIGHT_WALL:
                    ans.append(matrix[i][j])
                    j += 1
                i, j = i+1, j-1
                RIGHT_WALL -= 1
                direction = DOWN
            elif direction == DOWN:
                while i < DOWN_WALL:
                    ans.append(matrix[i][j])
                    i += 1
                i, j = i-1, j-1
                DOWN_WALL -= 1
                direction = LEFT
            elif direction == LEFT:
                while j > LEFT_WALL:
                    ans.append(matrix[i][j])
                    j -= 1
                i, j = i-1, j+1
                LEFT_WALL += 1
                direction = UP
            else:
                while i > UP_WALL:
                    ans.append(matrix[i][j])
                    i -= 1
                i, j = i+1, j+1
                UP_WALL += 1
                direction = RIGHT
        
        return ans