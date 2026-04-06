# 1456
# my solution ->

class Solution(object):
    def maxVowels(self, s, k):
        vowels = set('aeiou')
        count = 0

        for i in range(k):
            if s[i] in vowels:
                count += 1

        n = len(s)
        maxx = count
        for i in range(k, n):
            if s[i] in vowels:
                count += 1
            if s[i - k] in vowels:
                count -= 1
            
            maxx = max(count, maxx)

        return maxx