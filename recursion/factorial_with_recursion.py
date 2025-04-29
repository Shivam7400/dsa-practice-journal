"""
Problem: Factorial of a Number
Topics: Recursion, Iteration
"""

class Factorial:
    # Time Complexity: O(n)
    # Space Complexity: O(1) for iterative, O(n) for recursive due to call stack

    def recursive(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return n * self.recursive(n - 1)

    def iterative(self, n: int) -> int:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

fact = Factorial()
print(fact.recursive(5))
print(fact.iterative(5))