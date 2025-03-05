# Approach:
# Use a min-heap to store the smallest node from each list, maintaining the heap property.
# Continuously pop the smallest node, add it to the merged list, and push the next node from that list 
# (if available) into the heap.
# Time & Space Complexity:
# Time Complexity: O(N log k) where N is the total number of nodes across all lists and k is the number of lists (heap operations on k elements).
# Space Complexity: O(k) for the heap, as it stores one node from each of the k lists at a time.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        # Custom comparator for heap elements (value, index, node)
        heap = []
        # Step 1: Insert the first node of each list into the heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node)) # (value, index, node)
        # Dummy node to build the merged list
        dummy = ListNode()
        current = dummy
        # Step 2: Process the heap
        while heap:
            val, i, node = heapq.heappop(heap)  # Get the smallest value node
            current.next = node # Add to merged list
            current = current.next # Move pointer

            # If there is a next node in the list, push it to the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next  # Return the merged list

        