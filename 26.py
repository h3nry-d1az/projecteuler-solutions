__memo = {}
def pfactors(n: int) -> set:
    """Yields the prime factors of $n$."""
    if (f := __memo.get(n)): return f
    if n == 1: return set()
    for k in range(2, n+1):
        if n % k == 0:
            __memo[n] = {k} | pfactors(n//k)
            return __memo[n]

def cycle_length(d: int) -> int:
    """Returns the length of the period of $1/d$."""
    f = pfactors(d)
    if f <= {2, 5}: return 0
    if 2 in f or 5 in f:
        m = 0
        while (10**m * (10**(m+1) - 1)) % d != 0: m += 1
        i = 1
        while True:
            if 10**m*(10**i - 1) % d == 0: return i
            i += 1
    else:
        i = 1
        while True:
            if (10**i - 1) % d == 0: return i
            i += 1

main = lambda D: max(((d, cycle_length(d)) for d in range(2, D+1)), key=lambda p: p[1])[0]
main.__doc__ = """Solution entry point."""

if __name__ == '__main__':
    print(main(1000))