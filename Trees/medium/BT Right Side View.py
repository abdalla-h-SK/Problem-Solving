# 199
# my solution ->

#   Time : O(n)
#   Space: O(n)

from collections import deque
class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []

        list_of_nodes = []
        traversal_queue = deque([root])

        while len(traversal_queue) > 0:
            level = []
            n = len(traversal_queue)
            for i in range(n):
                node = traversal_queue.popleft()
                level.append(node.val)

                if node.left:
                    traversal_queue.append(node.left)
                if node.right:
                    traversal_queue.append(node.right)

            list_of_nodes.append(level)

        return list(map(lambda x:x[-1], list_of_nodes))