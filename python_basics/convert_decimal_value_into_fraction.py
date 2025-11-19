from fractions import Fraction
from typing import List

class RationalHelper:
    """
    This class converts a decimal value into:
      1. Simplified fraction
      2. Original (unsimplified) fraction
      3. A list of equivalent fractions
    """
    # Time Complexity: O(count) depend on number of count
    # Space Complexity: O(count) depend on number of count
    def __init__(self, value: float, count: int = 5):
        self.value = value
        self.count = count

    def generate_fractions(self) -> List:
        results = []

        # 1. Simplified fraction using Fraction
        frac = Fraction(self.value).limit_denominator()
        results.append(f"{frac.numerator}/{frac.denominator}")

        # 2. Original (unsimplified) fraction from decimal
        s = str(self.value)
        if '.' in s:
            decimal_places = len(s.split('.')[1])
            numerator = int(self.value * (10 ** decimal_places))
            denominator = 10 ** decimal_places
        else:
            numerator = int(self.value)
            denominator = 1

        results.append(f"{numerator}/{denominator}")

        # 3. Equivalent fractions list
        eq = []
        for i in range(2, self.count + 2):
            eq_num = frac.numerator * i
            eq_den = frac.denominator * i
            eq.append(f"{eq_num}/{eq_den}")
        results.append(eq)

        return results


if __name__ == "__main__":
    obj = RationalHelper(3.5, 5)
    print(obj.generate_fractions())
