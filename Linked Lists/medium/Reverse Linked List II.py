# 92

# my solution ->

#   Time : O(n)
#   Space: O(n)

class Solution(object):
    def reverseBetween(self, head, left, right):
        if left == right:
            return head
        k = right - left + 1
        pos  = 1
        curr = head
        prev = None
        while pos < left:
            pos += 1
            prev = curr
            curr = curr.next

        stack = []
        for i in range(k):
            stack.append(curr)
            curr = curr.next
        link = curr

        if left == 1:
                head = None
        else:
            curr = prev
        while stack:
            if not head:
                head = stack.pop()
                curr = head
            else:
                curr.next = stack.pop()
                curr = curr.next

        curr.next = link
        return head