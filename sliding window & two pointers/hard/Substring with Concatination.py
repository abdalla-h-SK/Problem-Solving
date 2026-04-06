# 30
# my solution -> after deepseek hints!

# It was giving me TLE bcz of Counter and defaultdict! wtf , and this soluiton is slow bcz of them!

from collections import defaultdict, Counter

class Solution(object):
    def findSubstring(self, s, words):
        k = len(words[0])
        n = len(words) * k
        counter = {}
        for w in words:
            if w in counter:
                counter[w] += 1
            else:
                counter[w] = 1

        ans = []

        for i in range(len(s) - n + 1):
            window = {}
            phrase = s[i:i + n]
            take = True

            for j in range(0, n, k):
                w = phrase[j:j + k]

                if w in window:
                    window[w] += 1
                else:
                    window[w] = 1
                
            if window == counter:
                ans.append(i)
        
        return ans