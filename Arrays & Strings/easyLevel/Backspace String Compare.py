# 844
# my solution ->

# Time : O(n), Space : O(1)

class Solution(object):
    def backspaceCompare(self, s, t):
        m, n = len(s), len(t)
        i, j = m - 1, n - 1

        back_i, back_j = 0, 0

        while i >= 0 or j >= 0:
            while i >= 0 and (s[i] == '#' or back_i > 0):

                if s[i] == '#':
                    back_i += 1
                else:
                    back_i -= 1

                i -= 1

            while j >= 0 and (t[j] == '#' or back_j > 0):
                
                if t[j] == '#':
                    back_j += 1
                else:
                    back_j -= 1

                j -= 1

            if (i >= 0 and j >= 0 and s[i] != t[j]) or (i < 0 and j >= 0) or (j < 0 and i >= 0):
                return False
            

            i -= 1
            j -= 1
        
        return True