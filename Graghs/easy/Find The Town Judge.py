# 997
# my solution ->

from collections import defaultdict

class Solution(object):
    def findJudge(self, n, trust):
        if n == 1:
            return 1 if not trust else -1

        ppl_ho_trust = set()
        trust_dict = defaultdict(list)

        for fan, trust_person in trust:
            trust_dict[trust_person].append(fan)
            ppl_ho_trust.add(fan)
        
        for trust_person, fans in trust_dict.items():
            if len(fans) == n - 1 and trust_person not in ppl_ho_trust:
                return trust_person
        
        return -1