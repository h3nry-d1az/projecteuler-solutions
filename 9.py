r"""# Special Pythagorean Triplet
## Problem Statement
A Pythagorean triplet is a set of three natural numbers, $a \lt b \lt c$, for which,
$$a^2 + b^2 = c^2.$$

For example, $3^2 + 4^2 = 9 + 16 = 25 = 5^2$.

There exists exactly one Pythagorean triplet for which $a + b + c = 1000$.<br>Find the product $abc$.

## Solution
From $a+b+c=1000$ follows that $c=1000-a-b$. Thus, we can iterate $a$ and $b$ up to $334$ and $500$ respectively (since $a< b < c$), check whether $a^2 + b^2 = c^2$ and, if so, print $abc$. The program outputs $\boxed{31875000}$ as a result."""

def solution() -> None:
  """Solution entry point."""
  for a in range(1, 334):
    for b in range(a, 500):
      if a**2 + b**2 == (c:=1000-a-b)**2:
        print(a*b*c) # 31875000
        return

if __name__ == '__main__': solution()