r"""# Factorial Digit Sum
**Problem:** $n!$ means $n \times (n - 1) \times \cdots \times 3 \times 2 \times 1$.

For example, $10! = 10 \times 9 \times \cdots \times 3 \times 2 \times 1 = 3628800$, and the sum of the digits in the number $10!$ is $3 + 6 + 2 + 8 + 8 + 0 + 0 = 27$.

Find the sum of the digits in the number $100!$.

**Solution:** Since Python has built-in support for bignums, and a factorial function within the `math` module, this problem is trivial."""

from math import factorial

def digits(n: int) -> list:
  """Returns a list containing the base-$10$ digits of $n$ in reverse order."""
  output = []
  while n >= 10:
    output.append(n%10)
    n //= 10
  output.append(n)
  return output

def solution() -> None:
  """Solution entry point."""
  print(sum(digits(factorial(100)))) # 648

solution()