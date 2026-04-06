# 102
from collections import deque
class Solution(object):
    def levelOrder(self, root):
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

        return list_of_nodes

    # Time Complexity: O(n)
    # Space Complexity: O(n)