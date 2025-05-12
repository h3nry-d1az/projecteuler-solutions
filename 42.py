r"""# Multiples of 3 or 5
## Problem Statement
The $n$<sup>th</sup> term of the sequence of triangle numbers is given by, $t_n = \frac12n(n+1)$; so the first ten triangle numbers are: $$1, 3, 6, 10, 15, 21, 28, 36, 45, 55, \dots$$

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is $19 + 11 + 25 = 55 = t_{10}$. If the word value is a triangle number then we shall call the word a triangle word.

Using <a href="https://projecteuler.net/resources/documents/0042_words.txt">words.txt</a> (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

## Solution
The only slight difficulty in this problem is checking whether a number is triangular, having that achieved, we can simply iterate through each word and proceed as described in the problem statement.

Recall that the sequence of triangular numbers is defined as $$t_n = \frac{n(n+1)}{2} = 1+2+3+\ldots+n,$$ so to check whether a number is triangular we may subtract $1$, $2$, etc. from it until it reaches either $0$ or a negative number, and then return `True` in the former case and `False` in the latter.

The execution of this algorithm yields $\boxed{162}$ as the number of words in <a href="https://projecteuler.net/resources/documents/0042_words.txt">words.txt</a> that are triangular."""

alphabet = "_ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def is_triangular(n: int) -> bool:
  """Outputs whether the input $n$ is a triangular number."""
  m = n
  k = 1
  while m > 0:
    m -= k
    k += 1
  return True if m == 0 else False

def solution() -> None:
  """Solution entry point."""
  counter = 0
  with open('words.txt') as words:
    for word in words.read().split(','):
      if is_triangular(sum(map(lambda c: alphabet.find(c), word[1:-1]))): counter += 1
  print(counter) # 162

if __name__ == '__main__': solution()