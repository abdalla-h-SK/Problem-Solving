# 48

class Solution:
    def rotate(self, matrix):
        
        n = len(matrix)
        
        # Tranpose
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Reflection
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]
        
        # Time: O(n^2)
        # Space: O(1)
    

# another solution ->

class Solution(object):
    def rotate(self, matrix):
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                topleft = matrix[top][l + i]
                
                matrix[top][l + i] = matrix[bottom - i][l]

                matrix[bottom - i][l] = matrix[bottom][r - i]

                matrix[bottom][r - i] = matrix[top + i][r]

                matrix[top + i][r] = topleft
            
            l += 1
            r -= 1