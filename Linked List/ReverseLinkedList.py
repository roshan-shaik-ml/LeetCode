"""
LeetCode [206]: Reverse Linked List

Given the head of a singly linked list, reverse the list, and return its head.

Approach:
Iteratively traverse the linked list, reversing the pointers of each node to point to the previous node instead of the next node.

Code with Comments:
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize three pointers: current, previous, and next
        current = head
        prev = None
        nxt = None
        # Iterate through the linked list
        while current != None:
            # Store the next node
            nxt = current.next
            # Reverse the pointer of the current node to point to the previous node
            current.next = prev
            # Move the pointers one step forward
            prev = current
            current = nxt
        # Update the head to point to the last node (previously the head)
        head = prev
        # Return the new head of the reversed linked list
        return head
