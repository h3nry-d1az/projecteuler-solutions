r"""# Pandigital Products
## Problem Statement
Take the number $192$ and multiply it by each of $1$, $2$, and $3$:

\begin{align}
192 \times 1 &= 192\\\\
192 \times 2 &= 384\\\\
192 \times 3 &= 576
\end{align}

By concatenating each product we get the $1$ to $9$ pandigital, $192384576$. We will call $192384576$ the concatenated product of $192$ and $(1,2,3)$.

The same can be achieved by starting with $9$ and multiplying by $1$, $2$, $3$, $4$, and $5$, giving the pandigital, $918273645$, which is the concatenated product of $9$ and $(1,2,3,4,5)$.

What is the largest $1$ to $9$ pandigital $9$-digit number that can be formed as the concatenated product of an integer with $(1,2, \dots, n)$ where $n \gt 1$?

## Solution
Notice first that it must hold that $n\leq 9$, since otherwise even $1\cdot(1, 2, \ldots, n) > 12345678910 > 999999999$, which is bigger than any pandigital number. We may use this same insight to find out that the corresponding $k$ to multiply $(1, 2, \ldots, n)$ must be smaller than $10^{\lceil \frac{9}{n} \rceil + 1}$.

Overall, this program iterates over all these possibilities and then prints the maximum of the valid candidates, which yields $\boxed{932718654}$ as the final, correct result.
"""

from math import ceil
from functools import reduce

def digits(n: int) -> list:
  """Returns a list containing the base-$10$ digits of $n$."""
  output = []
  while n >= 10:
    output.append(n%10)
    n //= 10
  output.append(n)
  return list(reversed(output))

def digits_to_number(digit_list: list) -> int:
  """Constructs a number from its digits."""
  result = 0
  for digit in digit_list:
    result *= 10
    result += digit
  return result

def solution() -> None:
  """Solution entry point."""
  candidates = set()
  for n in range(2, 10):
    for k in range(1, 10**ceil(9/n+1)):
      l = reduce(lambda a, b: a+b, (digits(k*i) for i in range(1, n+1)))
      if sorted(l) == list(range(1, 10)):
        candidates.add(digits_to_number(l))
  print(max(candidates)) # 932718654

if __name__ == '__main__': solution()