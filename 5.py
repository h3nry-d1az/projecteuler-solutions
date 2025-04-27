r"""# Smallest Multiple
**Problem:** $2520$ is the smallest number that can be divided by each of the numbers from $1$ to $10$ without any remainder.

What is the smallest positive number that is **evenly divisible** (divisible with no remainder) by all of the numbers from $1$ to $20$?

**Solution:** This is just $\operatorname{lcm}(1,2,\ldots,20)$, which is already built-in in the math module and yields $\boxed{232792560}$."""

from math import lcm

def solution() -> None:
  """Solution entry point."""
  print(lcm(*range(1, 21))) # 232792560

solution()