# 138
# my solution ->
#   Time : O(n) , Space : O(n)

class Node:
    pass
class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return

        cur = head
        node_map = dict()

        while cur:
            node_map[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            node_map[cur].next = node_map[cur.next] if cur.next else None
            node_map[cur].random = node_map[cur.random] if cur.random else None
            cur = cur.next
        
        return node_map[head]