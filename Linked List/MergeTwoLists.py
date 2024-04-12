"""
LeetCode [21]: Merge Two Sorted Lists

Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Approach:
1. Initialize two pointers, 'ptr1' and 'ptr2', to the heads of the input lists 'list1' and 'list2' respectively.
2. Create a dummy node to serve as the head of the merged list, and another pointer 'dummy' to keep track of the last node in the merged list.
3. Iterate through both lists simultaneously until either 'ptr1' or 'ptr2' becomes None.
4. Compare the values of 'ptr1' and 'ptr2', and append the smaller node to the merged list.
5. Move the corresponding pointer to the next node.
6. Once one of the lists is exhausted, append the remaining nodes of the other list to the merged list.
7. Return the next node of the dummy node, which represents the head of the merged list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize pointers to the heads of the input lists
        ptr1 = list1
        ptr2 = list2

        # Create a dummy node to serve as the head of the merged list
        dummy = ListNode()
        # Pointer to keep track of the last node in the merged list
        ans = dummy

        # Iterate through both lists simultaneously until either pointer becomes None
        while ptr1 is not None and ptr2 is not None:
            # Compare the values of the nodes and append the smaller node to the merged list
            if ptr1.val <= ptr2.val:
                temp = ptr1.next
                dummy.next = ptr1
                ptr1.next = None
                ptr1 = temp
                dummy = dummy.next
            else:
                temp = ptr2.next
                dummy.next = ptr2
                ptr2.next = None
                ptr2 = temp
                dummy = dummy.next

        # Append the remaining nodes of the other list to the merged list
        if ptr2 is not None:
            dummy.next = ptr2
        else:
            dummy.next = ptr1

        # Return the next node of the dummy node, which represents the head of the merged list
        return ans.next
