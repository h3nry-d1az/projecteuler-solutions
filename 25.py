r"""# $1000$-digit Fibonacci Number
**Problem:** The Fibonacci sequence is defined by the recurrence relation:
<blockquote>$F_n = F_{n - 1} + F_{n - 2}$, where $F_1 = 1$ and $F_2 = 1$.</blockquote>

Hence the first $12$ terms will be:
\begin{align}
F_1 &= 1\\\\
F_2 &= 1\\\\
F_3 &= 2\\\\
F_4 &= 3\\\\
F_5 &= 5\\\\
F_6 &= 8\\\\
F_7 &= 13\\\\
F_8 &= 21\\\\
F_9 &= 34\\\\
F_{10} &= 55\\\\
F_{11} &= 89\\\\
F_{12} &= 144
\end{align}

<p>The $12$th term, $F_{12}$, is the first term to contain three digits.</p>
<p>What is the index of the first term in the Fibonacci sequence to contain $1000$ digits?</p>

**Solution:** Recall that, given a number $n$ in base-$10$, its binary represantation is $$n = n_k n_{k-1} \cdots n_2n_1n_0 = n_0 10^0 + n_1 10^1 + \ldots + n_k 10^k,\qquad\text{where}\qquad 0\leq n_i \leq 9$$ so we want to find a mathematical function $d$ (digits of $n$) such that $d(n) = k+1$.

Notice now that $$k + 1 = \log 10^k + 1 \leq \log n + 1 < \log 10^{k+1} + 1 = k+2 \implies \lfloor \log n + 1\rfloor = k+1,$$ therefore, $d(n) = \lfloor \log n + 1\rfloor$ is what we were looking for. The problem can thus be solved with a `while` loop that checks whether $d(F_k) = 1000$, and the memoized Fibonacci implementation from problem two. Ultimately, the program returns $\boxed{4782}$."""

from math import log, floor

log10 = lambda x: log(x)/log(10)
log10.__doc__ = "Base-$10$ logarithm."

d = lambda n: floor(log10(n) + 1)
d.__doc__ = "Digits of $n$."

def fibo(n: int, memo: dict) -> int:
  """Returns the $n$th Fibonacci number."""
  if memo.get(n): return memo[n]
  else:
    memo[n] = fibo(n-1, memo) + fibo(n-2, memo)
    return memo[n]

def solution() -> None:
  """Solution entry point."""
  memo = {1: 1, 2: 1}
  k = 12
  while d(fibo(k, memo)) != 1000:
    k += 1
  print(k) # 4782

solution()