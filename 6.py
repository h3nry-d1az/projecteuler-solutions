r"""# Sum Square Difference
**Problem:** The sum of the squares of the first ten natural numbers is,
  $$1^2 + 2^2 + ... + 10^2 = 385.$$
  The square of the sum of the first ten natural numbers is,
  $$(1 + 2 + ... + 10)^2 = 55^2 = 3025.$$
  Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.
  Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

**Solution:** Recall that the sum of the $n$ first natural numbers can be reduced to the following expression $$1 + 2 + 3 + \ldots + n = \frac{n(n+1)}{2},$$ therefore, we can conclude that $$(1 + 2 + 3 + \ldots + n)^2 = \frac{n^2(n+1)^2}{4}. \tag{1}$$
  Similarly, the sum of the $n$ first perfect squares follows the formula below (easily proved by induction): $$1^2 + 2^2 + 3^2 + \ldots + n^2 = \frac{n(n+1)(2n+1)}{6}. \tag{2}$$
  Finally, plugging in $n=100$ and taking the difference of $(1)$ and $(2)$ yields $$\left|\frac{100(101)(201)}{6} - \frac{100^2(101)^2}{4}\right| = \boxed{25164150}.$$"""

def solution() -> None:
  """Solution entry point."""
  print(abs(100*101*201//6 - 100**2 * 101**2//4)) # 25164150

solution()