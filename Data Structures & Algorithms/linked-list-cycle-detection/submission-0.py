# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Let's do a hashset,
        # If the address of a node in the hashset is referenced
        # we know there's a cycle
        # Otherwise we will iterate and add nodes to the hashset
        # This will overall be an O(n) time and space approach
        # One pass for iteration, a hashset storing n things.
        seen = set()
        curr = head
        while curr != None:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next
        return False