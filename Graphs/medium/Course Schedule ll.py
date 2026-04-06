# 210
# my solution ->

    # Time : O(V + E)
    # Space: O(V + E)

from collections import defaultdict
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        gragh = defaultdict(list)
        for k, v in prerequisites:
            gragh[k].append(v)

        states = [0] * numCourses
        order_lst = []

        def dfs(node):
            state = states[node]
            if state == 2:
                return True
            elif state == 1:
                return False
            
            states[node] = 1

            for nei in gragh[node]:
                if not dfs(nei):
                    return False
            
            states[node] = 2
            order_lst.append(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []

        return order_lst