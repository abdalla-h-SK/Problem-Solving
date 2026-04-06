# 876

# my solution ->

#   Time : O(n)
#   Space: O(1)

class Solution:
    def middle(self, head):
        if not head or not head.next:
            return head
        
        a = head
        b = head

        while b and b.next:
            a = a.next
            b = b.next.next

        return a