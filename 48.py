r"""# Self Powers
## Problem Statement
<p>The series, $1^1 + 2^2 + 3^3 + \cdots + 10^{10} = 10405071317$.</p>
<p>Find the last ten digits of the series, $1^1 + 2^2 + 3^3 + \cdots + 1000^{1000}$.</p>"""

def exp10d(a: int, b: int) -> int:
  n = a
  m = b
  while m != 1:
    n = (n * a) % 10000000000 
    m -= 1
  return n

def solution() -> None:
  """Solution entry point."""
  print(sum(exp10d(n, n) for n in range(1, 1001)) % 10000000000)

if __name__ == '__main__': solution()