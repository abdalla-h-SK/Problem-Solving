# 28
# my solution ->

class Solution(object):
    def strStr(self, haystack, needle):
        m, n = len(haystack), len(needle)
        if m < n:
            return -1
        if m == n:
            return 0 if haystack == needle else -1

        for i in range(m - n + 1):
            if haystack[i:i+n] == needle:
                return i
        return -1

# another solution !
class Solution(object):
    def strStr(self, haystack, needle):

        return haystack.find(needle)

        # the find method will return -1 if not found so we can use it over index() method that will raise an error in that case!