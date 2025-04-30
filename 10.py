r"""# Summation of Primes
**Problem:** The sum of the primes below $10$ is $2 + 3 + 5 + 7 = 17$.

Find the sum of all the primes below two million.

**Solution:** The solution can be expressed as a Python one-liner with the aid of a primality-checking function. We simply need to filter the primes out of the numbers from $2$ to $2\,000\,000$ and compute their sum, which yields $\boxed{142913828922}$."""

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
  print(sum(filter(isprime, range(2,2_000_000)))) # 142913828922

if __name__ == '__main__': solution()