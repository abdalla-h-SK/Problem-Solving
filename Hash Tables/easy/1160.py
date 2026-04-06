# my solution ->
from collections import Counter

class Solution(object):
    def countCharacters(self, words, chars):
        n = len(words)
        words_list = [None] * n
        for i in range(n):
            words_list[i] = Counter(words[i])
        
        chars = Counter(chars)

        ans = 0
        for i in range(n):
            take = True
            for k, v in words_list[i].items():
                if v > chars[k]:
                    take = False
            
            if take:
                ans += len(words[i])
        
        return ans