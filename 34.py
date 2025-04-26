r"""# Digit Factorials
**Problem:** $145$ is a curious number, as $1! + 4! + 5! = 1 + 24 + 120 = 145$.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As $1! = 1$ and $2! = 2$ are not sums they are not included.

**Solution:** Notice first that the maximum sum of digit factorials that can be obtained with $n$ digits is trivially $9!n = 362880n$, that is, it exhibits a linear growth with respect to $n$. On the other hand, the number itself increases by $\mathscr{O}(10^{n-1})$, i.e., exponentially. We can conclude from this fact that, after a certain threshold, the equality will not hold anymore.

In order to calculate this limit value, consider a number $\underbrace{100\ldots0}_{n\text{ digits}} = 10^{n-1} > 9!n$, which, after simple computations, yields $n=8$ as the smallest possible value. Ultimately, it is only needed to iterate up to that number and add the values that meet the criteria -- process slightly optimized by precalculating the factorials from $0$ to $9$ (see `factorial09`) --, yielding $\boxed{40730}$ as the result of the problem."""

def factorial09(n: int) -> int:
  """Returns the pre-calculated factorial of a number between $0$ and $9$. If the number does not lie between that range, the function returns $0$."""
  match n:
    case 0: return 1
    case 1: return 1
    case 2: return 2
    case 3: return 6
    case 4: return 24
    case 5: return 120
    case 6: return 720
    case 7: return 5040
    case 8: return 40320
    case 9: return 362880
    case _: return 0

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
  counter = 0
  for i in range(10, 10**7+1):
    if sum(map(factorial09, digits(i))) == i:
      counter += i
  print(counter) # 40730

solution()