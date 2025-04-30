r"""# Largest Prime Factor
**Problem:** The prime factors of $13195$ are $5, 7, 13$ and $29$.

What is the largest prime factor of the number $600851475143$?

**Solution:** We can simply create a function named `prime_factors`, which outputs a set containing the prime factors of $n$ and extract its maximum.

For the algorithmics behind `prime_factors`, we'll just start with an empty set and iterate from $2$ to $n$, if $n$ is divisible by $i$, then we'll add $i$ to the set and and call `prime_factors(n/i)` recursively to union them with our set of factors and break the loop. In general, since $i$ is minimal, it is guaranteed to be prime, since all composite numbers are products of primes by the fundamental theorem of arithmetic.

Calling `max(prime_factors(600851475143))` yields $\boxed{6857}$ as a result."""

def prime_factors(n: int) -> set:
  """Returns a set containing the prime factors of $n$."""
  factors = set()
  for i in range(2, n+1):
    if n % i == 0:
      factors.add(i)
      factors |= prime_factors(n//i)
      break
  return factors

def solution() -> None:
  """Solution entry point."""
  print(max(prime_factors(600851475143))) # 6857

if __name__ == '__main__': solution()