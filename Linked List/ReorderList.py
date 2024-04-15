"""
LeetCode [143]: Reorder List

Given the head of a singly linked list, reorder it in-place such that:

- Nodes from the first half of the linked list are interleaved with nodes from the second half in reverse order.
- The original and reordered lists should occupy the same nodes. Do not create any new nodes.

Approach:
1. Find the middle of the linked list using the slow and fast pointer technique.
2. Split the linked list into two halves at the middle.
3. Reverse the second half of the linked list.
4. Merge the first and reversed second halves of the linked list by interleaving them.

Code with Comments:
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Get the size of the linked list
        n = 0
        node = head
        while(node != None):
            n += 1
            node = node.next
        
        # Get the center of the linked list
        breakpt = head
        for i in range(0, n // 2):
            breakpt = breakpt.next
        
        # Split the linked list into two halves
        second_half = breakpt.next
        breakpt.next = None
        
        # Reverse the second half of the linked list
        prev = None
        curr = second_half
        while(curr != None):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Merge the first and reversed second halves of the linked list
        ptr = head
        while(prev != None):
            temp1 = ptr.next
            temp2 = prev.next
            ptr.next = prev
            prev.next = temp1
            ptr = temp1
            prev = temp2
