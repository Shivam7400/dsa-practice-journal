"""
Problem: Reverse Array
Topics: Array, Two Pointers
"""
class ReverseArray:
    # Approach: Two Pointers
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverseArray(self, arr):
        left = 0
        right = len(arr) - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr
    
    # Approach: Swaping Elements
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverseArraySwap(self, a):
        n = len(a)
        for i in range(n // 2):
            temp = a[i]
            a[i] = a[n - i - 1]
            a[n - i - 1] = temp
        return a

if __name__ == "__main__":
    ra = ReverseArray()
    print(ra.reverseArray([1, 4, 3, 2, 6, 5]))
    print(ra.reverseArraySwap([1, 4, 3, 2, 6, 5]))