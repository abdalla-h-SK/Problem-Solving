# 240
# my solution -> ChatGpt Hint !!

#   Time : O(log (m * n))
#   Space: O(1)

class Solution(object):
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1

        while i < m and j >= 0:
            num = matrix[i][j]
            if num == target:
                return True
            elif num < target:
                i += 1
            else:
                j -= 1
        
        return False