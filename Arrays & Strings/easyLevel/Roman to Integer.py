# 13

# my solution ->

#   Time: O(n)
#   Space:O(n)

class Solution(object):
    def romanToInt(self, s):
        dict_Romans = {'I': 1 ,'V': 5 ,'X': 10 ,'L': 50 ,'C': 100 ,'D': 500 , 'M': 1000}

        s = ''.join(list(s)[::-1])

        output = dict_Romans[s[0]]

        s2 = s[1:]

        for idx, ref in enumerate(s2, start=1):
            if dict_Romans[ref] < dict_Romans[s[idx - 1]]:
                output -= dict_Romans[ref]
            else:
                output += dict_Romans[ref]

        return output
    
# another solution -> 

#   Time: O(n)
#   Space:O(n)

class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D': 500, 'M':1000}
        summ = 0
        n = len(s)
        i = 0
        
        while i < n:
            if i < n - 1 and d[s[i]] < d[s[i+1]]:
                summ += d[s[i+1]] - d[s[i]]
                i += 2
            else:
                summ += d[s[i]]
                i += 1
        
        return summ