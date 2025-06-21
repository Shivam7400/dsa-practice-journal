# Importent | Medium level
"""
Problem: Merge Intervals
Topics: Array, Sorting, Greedy, Interval Scheduling
"""
class Solution:
    # Time Complexity: O(n log n) — due to sorting
    # Space Complexity: O(n) — for the output list
    def merge(self, intervals):
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for current in intervals[1:]:
            prev = merged[-1]
            if current[0] <= prev[1]:
                prev[1] = max(prev[1], current[1])
            else:
                merged.append(current)

        return merged

if __name__ == "__main__":
    solution = Solution()

    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(solution.merge(intervals))

    intervals = [[1,4],[4,5]]
    print(solution.merge(intervals))
