r"""# Circular Primes
## Problem Statement
The number, $197$, is called a circular prime because all rotations of the digits: $197$, $971$, and $719$, are themselves prime.

There are thirteen such primes below $100$: $2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79$, and $97$.

How many circular primes are there below one million?

## Solution
Essentially, and provided that we have already constructed a robust enough primality-checking function (see problem 7), the only difficult aspect per se is to find all the rotations of the array of digits of each number.

In order to achieve that functionality, we can first create a copy of the input, from which we will remove its last element and insert it back in the head, repeating this process until the copy is identical to the input, yielding of course every step in the meanwhile.

Overall, after the final count is performed, this program outputs $\boxed{55}$ as the result."""

from math import floor, sqrt
from typing import Iterator

def isprime(n: int) -> bool:
  """Check whether $n$ is prime or not."""
  if n <= 1: return False
  for k in range(2, floor(sqrt(n))+1):
    if n % k == 0:
      return False
  return True

def digits(n: int) -> list:
  """Returns a list containing the base-$10$ digits of $n$ in reverse order."""
  output = []
  while n >= 10:
    output.append(n%10)
    n //= 10
  output.append(n)
  return output

def digits_to_number(digit_list: list) -> int:
  """Constructs a number from its digits."""
  result = 0
  for digit in digit_list:
    result *= 10
    result += digit
  return result

def rotations(array: list) -> Iterator:
  """Returns all possible rotations of a given list."""
  current = array.copy()
  yield current
  e = current.pop()
  current.insert(0, e)
  while current != array:
    yield current
    e = current.pop()
    current.insert(0, e)

def solution() -> None:
  """Solution entry point."""
  counter = 0
  for n in range(2, 1_000_000):
    if all(map(isprime, map(digits_to_number, rotations(list(reversed(digits(n))))))):
      counter += 1
  print(counter) # 55

if __name__ == '__main__': solution()