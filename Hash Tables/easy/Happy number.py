# 202
# my solution ->
#   Time : O(n)
#   Space: O(m), where m is the number of distinct sums encountered during the process.

class Solution(object):
    def isHappy(self, n):
        num = str(n)
        res = 0
        numbers = set()

        while True:

            for digit in num:
                res += int(digit) ** 2
                
            if res == 1:
                return True
            
            if res in numbers:
                return False
            numbers.add(res)

            num ,res = str(res), 0