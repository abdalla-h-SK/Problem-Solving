# my solution ->

class Solution(object):
    def getDecimalValue(self, head):
        ans = 0
        cur = head

        while cur:
            ans *= 2
            ans += cur.val

            cur = cur.next

        return ans