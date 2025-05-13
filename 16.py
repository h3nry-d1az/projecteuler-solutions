r"""# Power Digit Sum
## Problem Statement
<p>$2^{15} = 32768$ and the sum of its digits is $3 + 2 + 7 + 6 + 8 = 26$.</p>
<p>What is the sum of the digits of the number $2^{1000}$?</p>

## Solution
Again, since Python has built-in support for bignums, this problem is a one-liner. The result is $\boxed{1366}$."""

def solution() -> None:
  """Solution entry point."""
  print(sum(map(int, str(2**1000)))) # 1366

if __name__ == '__main__': solution()