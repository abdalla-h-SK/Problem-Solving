# 2095
# my solution ->

class ListNode:
    pass

class Solution(object):
    def deleteMiddle(self, head):
        if not (head and head.next):
            return None
            
        d = ListNode()
        d.next = head
        prev = d
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            prev = prev.next
            fast = fast.next.next

        prev.next = slow.next

        return head