r"""# Largest Exponential
**Problem:** Comparing two numbers written in index form like $2^{11}$ and $3^7$ is not difficult, as any calculator would confirm that $2^{11} = 2048 < 3^7 = 2187$.

However, confirming that $632382^{518061} > 519432^{525806}$ would be much more difficult, as both numbers contain over three million digits.

Using [base_exp.txt](https://projecteuler.net/resources/documents/0099_base_exp.txt) (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.

**Solution:** Notice that since $\log x$ is a strictly increasing function, then $${a_1}^{b_1} > {a_2}^{b_2} \iff b_1 \log a_1 > b_2 \log a_2.$$ Therefore, the problem simplifies to finding the line that maximizes the expression above, which is much easier to handle. Overall, calling `max(powers)[0]` yields $\boxed{709}$ as the line with the maximum power."""

from math import log

def solution() -> None:
  """Solution entry point."""
  with open("0099_base_exp.txt") as file:
    powers = list(map(lambda t: (t[0], *map(int, t[1].split(','))),
        enumerate(file.read().splitlines())))
    print(powers[0], )
    print(max(powers, key=lambda t: t[2]*log(t[1]))[0]+1) # 

solution()