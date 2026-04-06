# 141

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
            
# another solution ->

#   Time : O(n)
#   Space: O(1)

class Solution(object):
    def hasCycle(self, head):
        d = ListNode()
        d.next = head
        slow = fast = d

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow is fast:
                return True
            
        return False