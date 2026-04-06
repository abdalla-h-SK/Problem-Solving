# 24

# my solution -> we can use reverse nodes in k group code with setting k = 2 !!

#   Time : O(n)
#   Space: O(1)

class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        ret = head.next
        curr = head
        point = head.next

        while point:
            if point.next:
                next_point = point.next.next
            else:
                next_point = None
            
            if curr.next:
                next_curr = curr.next.next
            else:
                next_curr = None
            
            if next_curr and not next_point:
                curr.next, point.next = next_curr, curr
                return ret

            curr.next, point.next = next_point, curr
            curr, point = next_curr, next_point

        return ret