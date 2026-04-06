# 66
# my solution ->

class Solution(object):
    def plusOne(self, digits):
        number = 0
        for i in range(len(digits)):
            number += digits[i]
            number *= 10
        
        number /= 10
        number += 1
        
        ans = []
        while number != 0:
            pick = number % 10
            number /= 10

            ans.append(pick)
        
        ans.reverse()
        return ans