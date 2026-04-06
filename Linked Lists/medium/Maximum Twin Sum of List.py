# 2130
# my solution ->

class Solution(object):
    def pairSum(self, head):
        if not head.next.next:
            return head.val + head.next.val

        n = 0
        d = head
        while d:
            d = d.next.next
            n += 2

        nodes = {}

        curr = head
        i = 0       
        while i < n / 2:
            nodes[i] = curr.val
            curr = curr.next
            i += 1
        
        max_sum = 0
        while curr:
            max_sum = max(max_sum, curr.val + nodes[n-i-1])
            curr = curr.next
            i += 1
        
        return max_sum