# 83

# my solution ->

#   Time : O(n)
#   Space: O(n)

from collections import deque

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return None
            
        lst = deque([])
        curr = head
        while curr:
            if curr.val not in lst:
                lst.append(curr.val)
            curr = curr.next
        
        head = ListNode(lst.popleft())
        curr = head
        while lst:
            curr.next = ListNode(lst.popleft())
            curr = curr.next

        curr.next = None

        return head
    
# my second solution ->

#   Time : O(n)
#   Space: O(1)

class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return None

        prev = head
        curr = head.next

        while curr:
            if curr.val == prev.val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
                
        return head