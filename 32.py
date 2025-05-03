r"""# Pandigital Products
## Problem Statement
We shall say that an $n$-digit number is pandigital if it makes use of all the digits $1$ to $n$ exactly once; for example, the $5$-digit number, $15234$, is $1$ through $5$ pandigital.

The product $7254$ is unusual, as the identity, $39 \times 186 = 7254$, containing multiplicand, multiplier, and product is $1$ through $9$ pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a $1$ through $9$ pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

## Solution
The process of checking whether a product is pandigital is not difficult per se; provided that we have a `digits` function as we have previously constructed, we can evaluate whether the digits of $mn$, appended to those of $m$ and $n$ are exactly the list $1$ through $9$.

What can be trickier, though, (at least from my perspective) are the iteration bounds. Let $d(n)$ denote the number of digits of $n$ (i.e. `len(digits(n))`), we thus know that $$d(m) + d(n) + d(mn) = 9$$ in order for the product to be pandigital. We can approximate a lower bound for $d(mn)$ as $d(m)d(n)$, thus: $$d(m)+d(n) + d(m)d(n) \leq d(m)+d(n) + d(mn) = 9 \implies d(n) \leq \frac{9}{1+d(m)}.$$ Therefore, $m$ can freely range from $1$ to $10^4$ whereas $n$ will start at $1$ and end at $10^{9/(1+d(m))}$. Overall, the summation yields $\boxed{45228}$ as the final result.
"""

def digits(n: int) -> list:
  """Returns a list containing the base-$10$ digits of $n$ in reverse order."""
  output = []
  while n >= 10:
    output.append(n%10)
    n //= 10
  output.append(n)
  return output

def solution() -> None:
  """Solution entry point."""
  summ = 0
  products = set()
  for m in range(1, 10_000):
    dm = digits(m)
    for n in range(1, 10**(9//(1+len(dm)))):
      if (p:=m*n) in products:
        continue
      d = digits(n)
      d.extend(dm)
      d.extend(digits(p))
      if sorted(d) == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        products.add(p)
        summ += p
        print(m, n)
  print(summ) # 45228

if __name__ == '__main__': solution()