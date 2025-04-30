r"""# Totient Permutation
**Problem:** Euler's totient function, $\varphi(n)$ [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to $n$ which are relatively prime to $n$. For example, as $1, 2, 4, 5, 7$, and $8$, are all less than nine and relatively prime to nine, $\varphi(9)=6$.<br>The number $1$ is considered to be relatively prime to every positive number, so $\varphi(1)=1$.

Interestingly, $\varphi(87109)=79180$, and it can be seen that $87109$ is a permutation of $79180$.

Find the value of $n$, $1 \lt n \lt 10^7$, for which $\varphi(n)$ is a permutation of $n$ and the ratio $n/\varphi(n)$ produces a minimum.

**Solution (very slow*):** The idea behind the solution is analogue to that of problem 69. That being said, the only different aspect is to check whether $\varphi(n) \in \mathtt{P}(n)$, where $\mathtt{P}(n)$ denotes the digit permutations of $n$. Notice, though, that $\varphi(n) \leq n$, so we only need to consider the permutations smaller than $n$ itself -- which serves as slight optimization --, hence the function `smaller_permutations`. Finally, this script employs multithreading and should be preferably run in a Python binary with GIL disabled. After a considerably long execution time, this program yields $\boxed{8319823}$ as the final result.

*Execution took a total of $25\\!\\!:\\!\\!45.21$ (min:sec.ms) in an AMD Ryzen 5 5600X 6-Core processor, running no-GIL Python 3.13."""

from math import prod, sqrt, floor
from itertools import permutations

import threading

__memo: dict = {}
def prime_factors(n: int) -> set:
  """Returns a set containing the prime factors of $n$."""
  if (f := __memo.get(n)):
    return f
  factors = set()
  for i in range(2, floor(sqrt(n))+1):
    if n % i == 0:
      factors.add(i)
      factors |= prime_factors(n//i)
      break
  factors = factors if len(factors) != 0 else {n}
  __memo[n] = factors
  return factors

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

phi = lambda n: round(n*prod(map(lambda p: 1-1/p, prime_factors(n))))
phi.__doc__ = r"""Computes $\varphi(n)$ (Euler's totient function)."""

nphi = lambda n: prod(map(lambda p: p/(p-1), prime_factors(n)))
nphi.__doc__ = r"""Computes $n/\varphi(n)$."""

def __smaller_list_permutations(l: list) -> set:
  if len(l) <= 1:
    return [l]
  possibilities = set()
  for i, element in enumerate(l):
    if element > l[0]:
      continue
    l2 = l.copy()
    l2.pop(i)
    for p in (__smaller_list_permutations(l2) if element == l[0] else permutations(l2)):
      possibilities.add((element, *p))
  return possibilities

smaller_permutations = lambda n: set(map(digits_to_number, __smaller_list_permutations(list(reversed(digits(n))))))
smaller_permutations.__doc__ = """Returns a set with all the digit permutations of $n$ smaller than itself."""

threads = 12

__candidates = set()
def __thread_main(start: int) -> None:
  for n in range(start, int(1e7), threads):
    if phi(n) in smaller_permutations(n):
      __candidates.add(n)

def solution() -> None:
  """Solution entry point."""
  thread_list = []
  for i in range(threads):
    thread_list.append(threading.Thread(target=__thread_main, args=(i+2,)))
    thread_list[i].start()
  for thread in thread_list:
    thread.join()
  print(min(__candidates, key=nphi)) # 8319823, took 25:45.21

if __name__ == '__main__': solution()