# 143
# my solution ->

class Solution(object):
    def reorderList(self, head):
        if not head.next or not head.next.next:
            return head
        
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        grap = slow.next
        stack = []

        while grap:
            stack.append(grap)
            grap = grap.next

        slow.next = None

        prev, curr = head, head.next

        while stack:
            temp = stack.pop()
            prev.next = temp
            temp.next = curr

            prev = curr
            curr = curr.next

        return head