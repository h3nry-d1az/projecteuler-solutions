r"""# $10\,001$st Prime
**Problem:** By listing the first six prime numbers: $2, 3, 5, 7, 11$, and $13$, we can see that the $6$th prime is $13$.

What is the $10\,001$st prime number?


**Solution:** The problem becomes trivial with a primality-checking function, employing a while loop that breaks whenever the prime number count reaches $10\,001$. The $10\,001$st prime turns out to be $\boxed{104743}$."""

from math import floor, sqrt

def isprime(n: int) -> bool:
  """Check whether $n$ is prime or not."""
  if n <= 1: return False
  for k in range(2, floor(sqrt(n))+1):
    if n % k == 0:
      return False
  return True

def solution() -> None:
  """Solution entry point."""
  n = 1
  counter = 0
  while counter != 10001:
    n += 1
    if isprime(n): counter += 1
  print(n) # 104743

if __name__ == '__main__': solution()