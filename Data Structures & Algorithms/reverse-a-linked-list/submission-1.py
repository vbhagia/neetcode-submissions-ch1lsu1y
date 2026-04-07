# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        if curr != None:
            next = curr.next

        while curr != None:
            curr.next = prev
            prev = curr
            curr = next
            if curr != None:
                next = curr.next
        return prev
        