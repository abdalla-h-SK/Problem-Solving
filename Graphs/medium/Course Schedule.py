# 207
# my solution -> awsa5 7al fi tari5 ('-')

    # Time : O(V + E)
    # Space: O(V + E)

from collections import defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        gragh = defaultdict(list)
        for v, k in prerequisites:
            if k in gragh[v] or k == v:
                return False
            gragh[k].append(v)

        if not prerequisites:
            return True
            
        for i in range(len(prerequisites)):
            source = prerequisites[i][1]    
            visited = set()
            visited.add(source)
            stack = [source]

            while stack:
                node = stack.pop()
                for nei in gragh[node]:
                    if nei == source:
                        return False
                    if nei not in visited:
                        visited.add(nei)
                        stack.append(nei)
        return True  

# a wide better solution ->

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        gragh = defaultdict(list)
        for k, v in prerequisites:
            gragh[k].append(v)

        states = [0] * numCourses

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
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True         