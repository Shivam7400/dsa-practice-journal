# Importent | Easy Level
"""
Problem: Flatten a Nested List or Array
Topics: Iteration, Stack, Array, Recursion, List
"""
class Solution:
    # Using Iteration with Stack
    # Time Complexity: O(n) - where n is total number of elements
    # Space Complexity: O(n) - for the result list and the stack

    def flatten(self, nested_list):
        result = []
        stack = [nested_list]

        while stack:
            current = stack.pop()
            if isinstance(current, list):
                stack.extend(reversed(current))
            else:
                result.append(current)

        return result
    
    # Using Recursion
    # Time Complexity: O(n) - n is the number of total elements
    # Space Complexity: O(n) - to store the flattened list

    def flattenRecursion(self, nested_list):
        result = []

        def _flatten(lst):
            for item in lst:
                if isinstance(item, list):
                    _flatten(item)
                else:
                    result.append(item)

        _flatten(nested_list)
        return result


if __name__ == "__main__":
    obj = Solution()
    nested = [1, [2, [3, 4], 5], 6]
    print("Flattened list:", obj.flatten(nested))
    nested = [9, [1, 8, 3, [3, 2], 5], 4, [1, 6]]
    print("Flattened list Using Recursion:", obj.flattenRecursion(nested))
