from math import factorial

C = lambda n, r: factorial(n)/(factorial(r)*factorial(n-r))
C.__doc__ = r"""Find $\displaystyle\{n \choose r\}$."""

def main(k: int) -> int:
    """Solution entry point."""
    count = 0
    for n in range(1, k+1):
        i = n//2
        while C(n, i) > 1_000_000:
            count += 1 if i == n//2 and n % 2 == 0 else 2
            i -= 1
    return count

if __name__ == '__main__': print(main(100))