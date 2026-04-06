# 6

# my solution ->

#   Time : O(n)
#   Space: O(n)
class Solution(object):
    def convert(self, s, numRows):
        lst_output = [""] * numRows
        i = 0
        counter = 0

        if numRows == 1:
            return s
        
        while i < len(s):

            while counter < numRows:
                if i == len(s):
                    break
                counter += 1
                lst_output[counter - 1] += s[i]
                i += 1
            
            while counter > 1:
                if i == len(s):
                    break
                counter -= 1
                lst_output[counter - 1] += s[i]
                i += 1

        return ''.join(lst_output)
            

# another solution ->

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        i, d = 0, 1
        rows = [[] for _ in range(numRows)]

        for char in s:
            rows[i].append(char)
            if i == 0:
                d = 1
            elif i == numRows - 1:
                d = -1
            i += d

        for i in range(numRows):
            rows[i] = ''.join(rows[i])

        return ''.join(rows)
    
        # Time: O(n * numRows)
        # Space: O(n)   