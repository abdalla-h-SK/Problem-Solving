# 73
# my solution ->

class Solution(object):
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        zeros = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeros.append((i, j))
        
        for i, j in zeros:
            for r in range(m):
                matrix[r][j] = 0
            for c in range(n):
                matrix[i][c] = 0


# another solution with constant space!

class Solution(object):
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        rowZero = False # to separate between 0 in first row and 0 in first colomn

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        rowZero = True
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for r in range(m):
                matrix[r][0] = 0
        
        if rowZero:
            for c in range(n):
                matrix[0][c] = 0