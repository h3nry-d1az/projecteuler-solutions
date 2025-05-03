r"""# Square Digit Chains
## Problem Statement
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.</p>
For example,
\begin{align}
&44 \to 32 \to 13 \to 10 \to \mathbf 1 \to \mathbf 1\\\\
&85 \to \mathbf{89} \to 145 \to 42 \to 20 \to 4 \to 16 \to 37 \to 58 \to \mathbf{89}
\end{align}

Therefore any chain that arrives at $1$ or $89$ will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at $1$ or $89$.

How many starting numbers below ten million will arrive at $89$?

## Solution
There is not really any further intuition than simply creating a `chain` function which applies the described procedure until the number reaches either $1$ or $89$, and then count how many numbers end in the latter. The output of the program is $\boxed{8581146}$."""

def digits(n: int) -> list:
  """Returns a list containing the base-$10$ digits of $n$ in reverse order."""
  output = []
  while n >= 10:
    output.append(n%10)
    n //= 10
  output.append(n)
  return output

def chain(n: int) -> int:
  """Generate the number chain described in the problem statement."""
  k = n
  while k not in {1, 89}:
    k = sum(map(lambda n: n**2, digits(k)))
  return k

def solution() -> None:
  """Solution entry point."""
  counter = 0
  for n in range(1, 10_000_000):
    if chain(n) == 89: counter += 1
  print(counter) # 8581146

if __name__ == '__main__': solution()