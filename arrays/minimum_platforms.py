# Importent | Midium level
"""
Problem: Minimum No Of Platforms Required For A Railway 
Topics: Arrays, Greedy, Sorting, Two Pointers
"""
class MinimumPlatforms:
    # Time Complexity: O(NlogN)
    # Space Complexity: O(1)
    # Approach: Sort the arrival and departure times. Use two pointers to traverse both arrays.
    def find_min_platforms(self, arr, dep):
        n = len(arr)
        arr.sort()
        dep.sort()

        platforms_needed = 0
        max_platforms = 0
        i = j = 0

        while i < n and j < n:
            if arr[i] <= dep[j]:
                platforms_needed += 1
                i += 1
                max_platforms = max(max_platforms, platforms_needed)
            else:
                platforms_needed -= 1
                j += 1

        return max_platforms

if __name__ == "__main__":
    arr = [10, 12, 10, 11, 12]
    dep = [11, 13, 12, 12, 13]
    n = len(arr)
    find_min_platforms = MinimumPlatforms()
    print(find_min_platforms.find_min_platforms(arr, dep))
