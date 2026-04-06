# 111
from collections import deque

# I have another solution with dfs but bfs is better tho!

class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        que = deque()
        que.append((root, 1))

        while que:
            node, depth = que.popleft()
            if not (node.left or node.right):
                return depth

            if node.left:
                que.append((node.left, depth + 1))
            if node.right:
                que.append((node.right, depth + 1))