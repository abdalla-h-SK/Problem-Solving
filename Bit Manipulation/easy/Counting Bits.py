# 338
# my soluiton ->

#   Time : O(n * bits per number) , Space : O(n)

class Solution(object):
    def countBits(self, n):
        ans = [0] * (n + 1)
        for i in range(n, 0, -1):
            num = i
            count = 0
            while num != 0:
                count += 1
                num &= num - 1
            ans[i] = count
            
        return ans 

# another solution ->

class Solution(object):
    def countBits(self, n):
        ans = [0] * (n + 1)
        offset = 1
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
                ans[i] = 1
                continue
            
            ans[i] = 1 + ans[i - offset]
        
        return ans