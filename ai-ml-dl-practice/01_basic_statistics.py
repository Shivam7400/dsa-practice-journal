# Easy Level
"""
Problem: Calculate Mean, Median, and Mode
Topics: Arrays, HashMap, Sorting, Math
"""

from typing import List, Union
from collections import defaultdict

class Solution:
    # Time Complexity: O(n log n) due to sorting
    # Space Complexity: O(n) for frequency map in mode()

    def __init__(self, data: List[Union[int, float]]):
        self.data = sorted(data)

    def mean(self) -> float:
        return sum(self.data) / len(self.data)

    def median(self) -> float:
        n = len(self.data)
        mid = n // 2
        if n % 2 == 0:
            return (self.data[mid - 1] + self.data[mid]) / 2
        else:
            return self.data[mid]

    def mode(self) -> Union[int, float, List[Union[int, float]]]:
        frequency = defaultdict(int)
        for num in self.data:
            frequency[num] += 1

        max_count = max(frequency.values())
        modes = [k for k, v in frequency.items() if v == max_count]

        return modes[0] if len(modes) == 1 else modes


if __name__ == "__main__":
    data = [1, 2, 2, 3, 4]
    stats = Solution(data)
    print(f"Mean: {stats.mean()}")
    print(f"Median: {stats.median()}")
    print(f"Mode: {stats.mode()}")