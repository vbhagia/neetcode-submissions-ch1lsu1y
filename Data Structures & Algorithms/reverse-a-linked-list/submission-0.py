class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # to reverse a linked list, we just change the directions of the pointer
        prev = None
        curr = head
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev