# Important | Medium Level
'''
Problem: Top K Frequent Elements
Topics: Hash Table, Array, Bucket Sort
'''
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def topKFrequent(self, nums, k):
        freq_map = {} # Count frequencies manually
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        # Bucket sort based on frequencies
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]  # Index = frequency
        for num, freq in freq_map.items():
            buckets[freq].append(num)

        # Collect top K frequent elements
        result = []
        for i in range(n, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

if __name__ == "__main__":
    solution = Solution()

    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(solution.topKFrequent(nums, k))