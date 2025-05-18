"""
Problem: Search in Rotated Sorted Array
Topics: Array, Binary Search
"""
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

if __name__ == "__main__":

    search_rotated = Solution()
    print(search_rotated.search([4,5,6,7,0,1,2], 0))
    print(search_rotated.search([4,5,6,7,0,1,2], 3))
    print(search_rotated.search([1], 0))