"""
LeetCode [19]: Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Approach:
1. Initialize two pointers, 'fast' and 'slow', both pointing to the head of the list.
2. Move the 'fast' pointer forward by 'n' positions.
3. If 'fast' becomes None, it means the node to be removed is the head of the list. Return head.next in this case.
4. Otherwise, move both 'fast' and 'slow' pointers forward until 'fast' reaches the end of the list.
5. Now, 'slow' points to the node just before the node to be removed.
6. Update the next pointer of 'slow' to skip the node to be removed.
7. Return the head of the list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Initialize two pointers, 'fast' and 'slow', both pointing to the head of the list
        fast = head
        slow = head

        # Move the 'fast' pointer forward by 'n' positions
        for i in range(0, n):
            fast = fast.next

        # If 'fast' becomes None, remove the head node and return the updated head
        if fast is None:
            return head.next

        # Move both 'fast' and 'slow' pointers forward until 'fast' reaches the end of the list
        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        # Now, 'slow' points to the node just before the node to be removed
        # Update the next pointer of 'slow' to skip the node to be removed
        slow.next = slow.next.next

        # Return the head of the list
        return head
