r"""# Multiples of 3 or 5
**Problem:** If we list all the natural numbers below $10$ that are multiples of $3$ or $5$, we get $3, 5, 6$ and $9$. The sum of these multiples is $23$.

  Find the sum of all the multiples of $3$ or $5$ below $1000$.

**Solution:** This is primarily a math problem rather than a computer science one. Recall that all multiples of $3$ are of the form $3k$, with $k\in\mathbb{Z}$; likewise, all numbers divisible by $5$ can be expressed as $5k$.
  Overall, the sum of multiples of $3$ becomes
  $$3\cdot 1 + 3\cdot 2 + \ldots + 3\cdot\left\lfloor\frac{999}{3}\right\rfloor = 3 \left(1+2+\ldots+\left\lfloor\frac{999}{3}\right\rfloor\right) = 3\left(\frac{\lfloor 999/3\rfloor (\lfloor 999/3\rfloor + 1)}{2}\right),$$
  and in an analog manner, the sum of multiples of $5$ is $$5\left(\frac{\lfloor 999/5\rfloor (\lfloor 999/5\rfloor + 1)}{2}\right).$$
  Therefore, the total sum would become the sum of the two above, but notice that we are double counting multiples of $3$ and $5$ (i.e., of $15$), so we need to subtract them once. Therefore, the final result is:
  $$3\left(\frac{\lfloor 999/3\rfloor (\lfloor 999/3\rfloor + 1)}{2}\right) + 5\left(\frac{\lfloor 999/5\rfloor (\lfloor 999/5\rfloor + 1)}{2}\right) - 15\left(\frac{\lfloor 999/15\rfloor (\lfloor 999/15\rfloor + 1)}{2}\right) = \boxed{233168}$$"""

def solution() -> None:
  """Solution entry point."""
  print(3*((999//3)*(999//3 + 1)//2) + 5*((999//5)*(999//5 + 1)//2) - 15*((999//15)*(999//15 + 1)//2)) # 233168

if __name__ == '__main__': solution()