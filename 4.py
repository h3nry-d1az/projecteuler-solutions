r"""# Largest Palindrome Product
**Problem:** A palindromic number reads the same both ways. The largest palindrome made from the product of two $2$-digit numbers is $9009 = 91 \times 99$.

Find the largest palindrome made from the product of two $3$-digit numbers.

**Solution:** We can create a function called `is_palindrome` which returns `True` if the input string is palindromic. We can then double-iterate from $100$ to $999$ and check whether $nm$, when converted to a string, is palindromic, and if so append it to our collection of palindromic numbers. Ultimately, we return the maximum of that list, which turns out to be $\boxed{906609}$."""

def is_palindromic(sequence: str) -> bool:
  """Outputs whether a given sequence of characters is palindromic."""
  return sequence == sequence[::-1]

def solution() -> None:
  """Solution entry point."""
  palindromes = []
  for n in range(100, 1000):
    for m in range(100, 1000):
      if is_palindromic(str(n*m)):
        palindromes.append(n*m)
  print(max(palindromes))

if __name__ == '__main__': solution()