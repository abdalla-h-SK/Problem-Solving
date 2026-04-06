# 191
# my solution ->

# Time : O(log(n))
# Space: O(1)

class Solution(object):
    def hammingWeight(self, n):
        count = 0
        binary = bin(n)[2:]
        for bit in binary:
            if bit == '1':
                count += 1
        return count
    

# another solution ->

class Solution(object):
    def hammingWeight(self, n):
        count = 0
        while n != 0:
            count += 1
            n &= n-1
        return count
    
    # Time : O(1 bits)
    # Space: O(1)