"""
Problem: Maximum and minimum of an array 
Topics: Array
"""
class MinMaxArray:
    # Time Complexity: O(N)
    # Auxiliary Space: O(1)
    def set_min(self, A):
        mini = float('inf')
        for num in A:
            if num < mini:
                mini = num
        return mini

    def set_max(self, A):
        maxi = float('-inf')
        for num in A:
            if num > maxi:
                maxi = num
        return maxi

if __name__ == "__main__":
    A = [4, 9, 6, 5, 2, 3]
    N = len(A)
    find_maax_and_min_value_of_arraay = MinMaxArray()
    print(f"Minimum element is:", find_maax_and_min_value_of_arraay.set_min(A))
    print("Maximum element is:", find_maax_and_min_value_of_arraay.set_max(A))