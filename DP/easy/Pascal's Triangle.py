# 118
# my solution ->

class Solution(object):
    def generate(self, numRows):
        res = [[1]]
        memo = {1:1}
        def pascal(row):
            if row in memo:
                return memo[row]
            
            lst = []
            for i in range(row):
                val = 0
                if i > 0:
                    val += res[pascal(row - 1) - 1][i - 1]
                if i < row - 1:
                    val += res[pascal(row - 1) - 1][i]

                lst.append(val)

            res.append(lst)
            memo[row] = row
            return row

        pascal(numRows)
        return res