# 2300
# my solution ->

class Solution(object):
    def successfulPairs(self, spells, potions, success):
        n, m = len(spells), len(potions)
        pairs = [0] * n
        peak = max(potions)
        potions.sort()

        for i in range(len(spells)):
            if spells[i] * peak < success:
                continue
            l, r = 0, m - 1
            while l < r:
                k = (l + r) // 2
                if spells[i] * potions[k] >= success:
                    r = k
                else:
                    l = k + 1
            
            pairs[i] = m - l
        
        return pairs