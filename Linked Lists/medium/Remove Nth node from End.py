# 19.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# my solution ->

#   Time : O(n)
#   Space : O(1)

class Solution(object):
    def removeNthFromEnd(self, head, n):
        count, Nth_from_begging = self.reinvet(head, n)
        if Nth_from_begging <= 0 or Nth_from_begging > count:
            return None
        if count == 1 and Nth_from_begging == 1:
            return None
        
        if Nth_from_begging == 1:
            head = head.next
            return head
        
        temp = 2
        curr = head.next
        prev = head
        for i in range(1, Nth_from_begging - 1):
            prev = curr
            curr = curr.next
            temp += 1

        if temp == count:
            prev.next = None
            curr = None
        else:
            prev.next = curr.next
            curr = None
        return head
    
    def reinvet(self, head, n):
        if not head:
            return 0
        
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        Nth_from_begging = count - n + 1

        return count, Nth_from_begging
    

# another solution -> great!
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode()
        dummy.next = head
        behind = ahead = dummy

        for _ in range(n + 1):
            ahead = ahead.next

        while ahead:
            behind = behind.next
            ahead = ahead.next

        behind.next = behind.next.next

        return dummy.next

# Time Complexity: O(n)
# Space Complexity: O(1)