# 133
class Node:
    pass

class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None
        point = node

        nodes = {}
        stack = [node]
        visited = set()
        while stack:
            node = stack.pop()
            nodes[node] = Node(val=node.val)

            for nei in node.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    stack.append(nei)


        for old, new in nodes.items():
            for nei in old.neighbors:
                new.neighbors.append(nodes[nei])

        return nodes[point]