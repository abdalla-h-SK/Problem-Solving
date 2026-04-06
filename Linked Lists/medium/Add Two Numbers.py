# 2

# my solution ->

#   Time : O(n)
#   Space: O(n)

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        sum = 0
        multiple = 1
        while l1 :
            sum += l1.val * multiple
            l1 = l1.next
            multiple *= 10

        multiple = 1
        while l2 :
            sum += l2.val * multiple
            l2 = l2.next
            multiple *= 10

        sum = str(sum)

        head = ListNode(int(sum[-1]))
        curr = head

        for i in range(len(sum) - 2, -1, -1):
            curr.next = ListNode(int(sum[i]))
            curr = curr.next
        curr.next = None

        return head        