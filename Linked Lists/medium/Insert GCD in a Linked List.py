# 2807

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# my solution ->

#   Time : O(n log(m))
#   Space : O(1)

class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        curr = head
        prev = None

        while curr.next:
            prev = curr
            curr = curr.next

            a, b = prev.val, curr.val
            if a < b:
                a, b = b, a

            while b != 0:
                a, b = b, a % b
            gcd = a

            i_node = ListNode(gcd)
            prev.next = i_node
            i_node.next = curr

        return head
    

# another solution ->
import math

class Solution:
    def insertGreatestCommonDivisors(self, head):
        prev = head
        cur = head.next
        
        while cur:
            gcd = math.gcd(cur.val, prev.val) # A
            g = ListNode(gcd)
            prev.next = g
            g.next = cur
            prev = cur
            cur = cur.next

        return head

# Time Complexity: O(n * A)
# Space Complexity: O(1)