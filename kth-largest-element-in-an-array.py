# Approach:
# Use a min-heap of size k, pushing elements from nums.
# If the heap exceeds k elements, remove the smallest (heappop), ensuring the heap always contains the k largest elements. 
# The top (heap[0]) is the kth largest.
# Time & Space Complexity:
# Time Complexity: O(N log k) (each push and pop operation takes O(log k), done N times).
# Space Complexity: O(k) (heap stores k elements at a time).
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap =[]
        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]





