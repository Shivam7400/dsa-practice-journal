# Medium Level
"""
Problem: Kth Largest Element in an Array
Topics: Array, Heap (Priority Queue), Sorting
"""
import heapq

class Solution:
    # Time Complexity: O(n log k), where n is the number of elements in nums
    # Space Complexity: O(k) for the heap
    def __init__(self, nums: list[int]):
        self.nums = nums

    def findKthLargest(self, k: int) -> int:
        # Min-heap of size k
        min_heap = self.nums[:k]
        heapq.heapify(min_heap)

        for num in self.nums[k:]:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)

        return min_heap[0]

if __name__ == "__main__":
    obj = Solution([3, 2, 1, 5, 6, 4])
    k = 2
    print(f"{k}th largest element:", obj.findKthLargest(k))
