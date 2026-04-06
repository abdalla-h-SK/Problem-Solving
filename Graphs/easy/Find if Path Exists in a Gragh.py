# 1971
# my solution ->

#   Time : O(n + E)
#   Space: O(n + E)

from collections import defaultdict
class Solution(object):
    def validPath(self, n, edges, source, destination):
        gragh = defaultdict(list)
        for k, v in edges:
            gragh[k].append(v)
            gragh[v].append(k)
        
        visited = set()
        visited.add(source)
        stack = [source]

        while stack:
            node = stack.pop()
            if node == destination:
                return True
            for nei in gragh[node]:
                if nei not in visited:
                    visited.add(nei)
                    stack.append(nei)
                
        return False