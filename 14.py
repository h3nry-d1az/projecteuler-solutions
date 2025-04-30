r"""# Longest Collatz Sequence
## Problem Statement
The following iterative sequence is defined for the set of positive integers:
* $n \to n/2$ ($n$ is even)
* $n \to 3n + 1$ ($n$ is odd)

  Using the rule above and starting with $13$, we generate the following sequence:
  $$13 \to 40 \to 20 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1.$$
  It can be seen that this sequence (starting at $13$ and finishing at $1$) contains $10$ terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at $1$.
  
  Which starting number, under one million, produces the longest chain?
  
  **NOTE:** Once the chain starts the terms are allowed to go above one million.

## Solution
Its feasible to simply brute-force the problem. Here, I just define a `collatz` function which outputs the length of the chain produced by $n$, and compute the argument of the maximum for `collatz(n)` where $n$ ranges between $13$ (which is already known), and $999999$. This yields $\boxed{837799}$ as the final solution."""

def collatz(n):
  """Compute the length of the chain produced by applying the Collatz sequence rules to the input $n$."""
  length = 1
  while n != 1:
    if n % 2 == 0:
      n /= 2
    else:
      n = 3*n + 1
    length += 1
  return length

def solution() -> None:
  """Solution entry point."""
  maximum = 13,10
  for n in range(13,999_999):
    if (c := collatz(n)) > maximum[1]:
      maximum = n,c
  print(maximum[0]) # 837799

if __name__ == '__main__': solution()
