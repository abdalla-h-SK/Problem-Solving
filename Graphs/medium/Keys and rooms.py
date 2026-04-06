# 841 
# my solution ->

class Solution(object):
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        gragh = dict()
        for i in range(n):
            gragh[i] = rooms[i]
        
        stack = [0]
        visited = set()
        visited.add(0)

        while stack:
            node = stack.pop()
            for nei in gragh[node]:
                if nei not in visited:
                    visited.add(nei)
                    stack.append(nei)
                    
        if len(visited) < n:
            return False
        return True