# 605
# my soluiton ->

#   Time : O(n)
#   Space: O(1)

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        j = len(flowerbed)

        if n == 0:
            return True

        for i in range(j):
            if flowerbed[i] != 0:
                continue

            val = 0
            
            if i > 0 and flowerbed[i-1] == 1:
                val += 1
            if i < j-1 and flowerbed[i+1] == 1:
                val += 1
        
            if val == 0:
                flowerbed[i] = 1
                n -= 1
        
            if n == 0:
                return True
        
        return False