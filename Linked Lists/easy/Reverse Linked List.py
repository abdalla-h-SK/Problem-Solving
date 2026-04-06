# 206
# my solution ->

#   Time : O(n) , Space : O(1)

class Solution(object):
    def reverseList(self, head):
        curr, prev = head, None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev