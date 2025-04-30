r"""# Totient Maximum
**Problem:** Euler's totient function, $\varphi(n)$ [sometimes called the phi function], is defined as the number of positive integers not exceeding $n$ which are relatively prime to $n$. For example, as $1$, $2$, $4$, $5$, $7$, and $8$, are all less than or equal to nine and relatively prime to nine, $\varphi(9)=6$.

<div style="text-align: center;">
<table style="margin-left: auto; margin-right: auto;"><tr><td><b>$n$</b></td>
<td><b>Relatively Prime</b></td>
<td><b>$\varphi(n)$</b></td>
<td><b>$n/\varphi(n)$</b></td>
</tr><tr><td>2</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr><tr><td>3</td>
<td>1,2</td>
<td>2</td>
<td>1.5</td>
</tr><tr><td>4</td>
<td>1,3</td>
<td>2</td>
<td>2</td>
</tr><tr><td>5</td>
<td>1,2,3,4</td>
<td>4</td>
<td>1.25</td>
</tr><tr><td>6</td>
<td>1,5</td>
<td>2</td>
<td>3</td>
</tr><tr><td>7</td>
<td>1,2,3,4,5,6</td>
<td>6</td>
<td>1.1666...</td>
</tr><tr><td>8</td>
<td>1,3,5,7</td>
<td>4</td>
<td>2</td>
</tr><tr><td>9</td>
<td>1,2,4,5,7,8</td>
<td>6</td>
<td>1.5</td>
</tr><tr><td>10</td>
<td>1,3,7,9</td>
<td>4</td>
<td>2.5</td>
</tr></table></div>

It can be seen that $n = 6$ produces a maximum $n/\varphi(n)$ for $n\leq 10$.

Find the value of $n\leq 1\,000\,000$ for which $n/\varphi(n)$ is a maximum.

**Solution:** Recall two fundamental properties of Euler's totient function: that $\varphi(mn)=\varphi(m)\varphi(n)$ whenever $m$ and $n$ are coprime, and that $\varphi(p^\alpha) = p^\alpha - p^{\alpha - 1}$ for a prime $p$ and an integer $\alpha$. Notice also that, by the fundamental theorem of arithmetic, we can express any given integer $n$ as a product of exponentiated primes ($n={p_1}^{\alpha_1}{p_2}^{\alpha_2}\cdots {p_n}^{\alpha_n}$). Applying the previous two lemmas to the expression above we reach a simplified, closed expression for $\varphi(n)$:
$$\varphi(n) = \varphi\left(\prod_{i=1}^k {p_i}^{\alpha_i}\right) = \prod_{i=1}^k \varphi({p_i}^{\alpha_i}) = \prod_{i=1}^k {p_i}^{\alpha_i} - {p_i}^{\alpha_i - 1}\prod_{i=1}^k {p_i}^{\alpha_i}\left(1-\frac{1}{p_i}\right) = n\prod_{i=1}^k \left(1-\frac{1}{p_i}\right).$$

Furthermore, for $n/\varphi(n)$, it follows that $$\frac{n}{\varphi(n)} = \frac{n}{n\prod_{i=1}^k \left(1-\frac{1}{p_i}\right)} = \frac{1}{\prod_{i=1}^k \frac{p_i - 1}{p_i}} = \prod_{i=1}^k \frac{p_i}{p_i-1}.$$

In conclusion, we only demand a decent function that extracts the prime factors for any given $n$ -- not even their powers! --, which can be implemented with recursion and memoization as seen in problem 3. The final output of the program yields $\boxed{510510}$ as the number under $1\,000\,000$ that maximizes $n/\varphi(n)$."""

from math import prod, sqrt, floor

__memo: dict = {}
def prime_factors(n: int) -> set:
  """Returns a set containing the prime factors of $n$."""
  if (f := __memo.get(n)):
    return f
  factors = set()
  for i in range(2, floor(sqrt(n))+1):
    if n % i == 0:
      factors.add(i)
      factors |= prime_factors(n//i)
      break
  factors = factors if len(factors) != 0 else {n}
  __memo[n] = factors
  return factors

def solution() -> None:
  """Solution entry point."""
  candidates = set()
  for n in range(2, 1_000_000+1):
    candidates.add((n, prod(map(lambda p: p/(p-1), prime_factors(n)))))
  print(max(candidates, key=lambda t: t[1])[0]) # 510510

if __name__ == '__main__': solution()