# Important | Medium Level
"""
Problem: Move all negative numbers to beginning and positive to end
Topics: Array, Two Pointers, In-Place Partition
"""
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)    
    def rearrange(self, arr: list[int]) -> None:
        j = 0
        for i in range(len(arr)):
            if arr[i] < 0:
                if i != j:
                    arr[i], arr[j] = arr[j], arr[i]
                j += 1

if __name__ == "__main__":
    arr = [1, -2, 3, -4, -1, 4, -5, 6]
    print("Original Array:", arr)

    sol = Solution()
    sol.rearrange(arr)

    print("Rearranged Array:", arr)
