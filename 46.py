r"""# Goldbach's Other Conjecture
**Problem:** It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
\begin{align}
9 = 7 + 2 \times 1^2\\\\
15 = 7 + 2 \times 2^2\\\\
21 = 3 + 2 \times 3^2\\\\
25 = 7 + 2 \times 3^2\\\\
27 = 19 + 2 \times 2^2\\\\
33 = 31 + 2 \times 1^2
\end{align}

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?


**Solution:** The conjecture can be rewritten equivalently as "for every odd number $2n+1$, there exists a number $k$ such that $(2n+1)-2k^2$ is prime". A valid counterexample would show that, for some $2n+1$, no such $k$ exists.

Notice first that a simple primality checking function can be implemented by iterating the numbers from $1$ to $\lfloor\sqrt n\rfloor$ and checking whether any one of them divides $n$. Another remarkable fact to take into account is that we only need to check for the $k$s lower than or equal to $\lceil\sqrt n\rceil$, since a number above that threshold would make the subtraction less than or equal to one, and thus not prime.

That being said, we can now employ a `while` loop that breaks whenever the condition is not satisfied, and print such number. The result turns out to be $\boxed{5777}$."""

from math import floor, ceil, sqrt

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
  while True:
    satisfies = False
    for k in range(0, ceil(sqrt(n))+1):
      if isprime(2*n+1-2*k**2):
        satisfies = True
    if not satisfies:
      break
    n += 1
  print(2*n+1) # 5777

if __name__ == '__main__': solution()