# 383

#   time : O(m + n)
#   space: O(m)

from collections import defaultdict
from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        
        counter = defaultdict(int)  # This is some how faster than the Counter
        for c in magazine:
            counter[c] += 1


######################################


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        
        counter = Counter(magazine)

        for item in ransomNote:
            if item not in counter:
                return False
            
            elif counter[item] == 1:
                del counter[item]

            else:
                counter[item] -= 1

        return True