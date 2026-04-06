# 203
# my solution ->

class Solution(object):
    def removeElements(self, head, val):
        while head and val == head.val:
            head = head.next

        if not head:
            return None

        prev, cur = None, head
        while cur:
            if cur.val == val:
                cur = cur.next
                prev.next = cur
                continue
                
            prev = cur
            cur = cur.next
        
        return head