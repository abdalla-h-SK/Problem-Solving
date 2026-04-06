# 849
# my solution

class Solution(object):
    def maxDistToClosest(self, seats):
        n = len(seats)
        cls_r = cls_l = float('inf')
        arr_r = [0] * n
        arr_l = [0] * n

        for i in range(n):
            j = -i-1

            if seats[i] == 1:
                cls_l = 0
            else:
                cls_l += 1
            
            if seats[j] == 1:
                cls_r = 0
            else:
                cls_r += 1

            arr_l[i] = cls_l
            arr_r[j] = cls_r

        ans = 0
        for l, r  in zip(arr_l, arr_r):
            ans = max(min(l, r), ans)
        
        return ans