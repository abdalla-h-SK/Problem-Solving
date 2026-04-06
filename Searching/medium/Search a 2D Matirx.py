# 74
# my solution ->

#   Time : O(m * log (n))
#   Space: O(1)

class Solution(object):
    def searchMatrix(self, matrix, target):
        for i in range(len(matrix)):
            l = 0
            r = len(matrix[i]) - 1

            while l <= r:
                m = (l + r) // 2
                
                if matrix[i][m] == target:
                    return True
                elif matrix[i][m] > target:
                    r = m - 1
                else:
                    l = m + 1
            
            continue
        
        return False
    
# another chatGpt solution with O(log (m * n)) time compexity ->

class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        
        m = len(matrix) 
        n = len(matrix[0])  
        
        l, r = 0, m * n - 1  
        
        while l <= r:
            mid = (l + r) // 2
       
            mid_val = matrix[mid // n][mid % n] # a tricky line 
            
            if mid_val == target:
                return True
            elif mid_val < target:
                l = mid + 1 
            else:
                r = mid - 1
        
        return False