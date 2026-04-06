# 367

#   Time : O(log (n))
#   Space: O(1)

class Solution(object):
    def isPerfectSquare(self, num):
        l = 1
        r = num

        while l <= r:
            m = (l + r) // 2
            m_squared = m * m

            if m_squared == num:
                return True
            elif m_squared < num:
                l = m + 1
            else:
                r = m - 1
                
        return False