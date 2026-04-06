# 443
# my solution ->
    
class Solution(object):
    def compress(self, chars):
        chars.append('Edge Case')
        n, count, j = len(chars), 1, 0

        for i in range(1, n):
            if chars[i] != chars[i-1]:

                chars[j] = chars[i-1]
                j += 1

                if count > 1:
                    for digit in str(count):
                        chars[j] = digit
                        j += 1

                count = 0
                
            count += 1
        
        return j if n > 1 else 1