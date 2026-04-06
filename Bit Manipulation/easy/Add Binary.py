# 67
# my solution ->

#   Time : O(n)
#   Space: O(1)

class Solution(object):
    def addBinary(self, a, b):

        b = b.zfill(len(a))
        a = a.zfill(len(b))

        ans = ''
        out = 0
        for i in range(len(a)-1, -1, -1):
            if a[i] == '0' and b[i] == '0':
                if not out:
                    ans += '0'
                else:
                    ans += '1'
                    out = 0
            
            elif a[i] == '1' and b[i] == '1':
                if not out:
                    ans += '0'
                    out = 1
                else:
                    ans += '1'
            
            else:
                if not out:
                    ans += '1'
                else:
                    ans += '0'

        if out:
            ans += '1'
        
        return ans[::-1]

# another solution ->

class Solution(object):
    def addBinary(self, a, b):
        a, b = int(a, 2), int(b, 2)

        while b:
            without_carry = a ^ b
            carry = (a & b) << 1
            a, b = without_carry, carry
        
        return bin(a)[2:]

    # Time : O (m + n)
    # Space: O (1)