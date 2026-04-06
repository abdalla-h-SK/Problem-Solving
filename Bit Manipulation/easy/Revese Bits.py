# 190

class Solution:
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res |= bit << (31 - i)
        return res
    
# my solution ->  but the above is better though!

class Solution:
    def reverseBits(self, n):
        lst = []
        offset = 1
        for i in range(32):
            temp = n
            if temp & offset == 0:
                lst.append('0')
            else:
                lst.append('1')
            offset <<= 1
        
        ans = "".join(lst)
        return int(ans, 2)