"""
LeetCode [4]: Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Approach:
1. Merge the two sorted arrays into a single sorted array.
2. If the total number of elements in the merged array is even, return the average of the middle two elements.
3. If the total number of elements in the merged array is odd, return the middle element.
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Merge the two sorted arrays into a single sorted array
        arr = self.getSorted(nums1, nums2)
        n = len(arr)
        # Check if the total number of elements in the merged array is even
        if n % 2 == 0:
            # If even, return the average of the middle two elements
            return (arr[n//2 - 1] + arr[n//2]) / 2
        # If odd, return the middle element
        return arr[n // 2]

    def getSorted(self, nums1, nums2):
        i = 0
        j = 0
        arr = []

        # Merge the two sorted arrays using two pointers
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1

        # If any array still has elements left, add them to the merged array
        if i == len(nums1):
            while j < len(nums2):
                arr.append(nums2[j])
                j += 1
        elif j == len(nums2):
            while i < len(nums1):
                arr.append(nums1[i])
                i += 1
        return arr
