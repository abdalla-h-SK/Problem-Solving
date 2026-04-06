# 21

# my solution ->

#   Time : O(m + n)
#   Space: O(1)

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):

        if not list1 and not list2:
            return None
        
        head = None
        curr1 = list1
        curr2 = list2

        while curr1 or curr2:

            if not curr1 or not curr2:
                if not curr1:
                    if head:
                        curr.next = curr2
                    else:
                        return curr2
                elif not curr2:
                    if head:
                        curr.next = curr1
                    else:
                        return curr1
                
                return head

            if curr1.val <= curr2.val:
                if not head:
                    head = ListNode(curr1.val)
                    curr = head
                else:
                    curr.next = ListNode(curr1.val)
                    curr = curr.next

                curr1 = curr1.next

            else:
                if not head:
                    head = ListNode(curr2.val)
                    curr = head
                else:
                    curr.next = ListNode(curr2.val)
                    curr = curr.next

                curr2 = curr2.next

# my second solution ->

#   Time : O(m + n)
#   Space: O(1)     

class Solution(object):
    def mergeTwoLists(self, list1, list2):

        if not list1 and not list2:
            return None
        elif not list1 and list2:
            return list2
        elif list1 and not list2:
            return list1

        if list1.val > list2.val:
            list1, list2 = list2, list1
        
        curr1 = list1
        curr2 = list2

        while curr1 or curr2:
            if not curr1.next:
                curr1.next = curr2
                return list1
            if not curr2:
                return list1
            
            if curr1.val <= curr2.val <= curr1.next.val:
                print(curr1.val, curr2.val, curr1.next.val)

                next_curr2 = curr2.next

                curr2.next = curr1.next
                curr1.next = curr2
                
                curr2 = next_curr2
            
            curr1 = curr1.next        

# another solution ->

class Solution:
    def mergeTwoLists(self, list1, list2):
        d = ListNode()
        cur = d

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                cur = list1
                list1 = list1.next
            else:
                cur.next = list2
                cur = list2
                list2 = list2.next

        cur.next = list1 if list1 else list2

        return d.next

# Time Complexity: O(n)
# Space Complexity: O(1)
